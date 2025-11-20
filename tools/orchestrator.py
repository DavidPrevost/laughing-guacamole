"""
Orchestrator - Central control system with approval gates

This system coordinates all other tools and ensures that actions requiring
human oversight are properly gated. It cannot autonomously perform any
action listed in CONSTRAINTS.md as requiring approval.
"""

import logging
from datetime import datetime
from enum import Enum
from typing import Any
from dataclasses import dataclass, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('orchestrator')


class ActionType(Enum):
    """Categories of actions the system can perform."""
    # Autonomous actions (no approval needed)
    GENERATE_CODE = "generate_code"
    RUN_LOCAL_TEST = "run_local_test"
    ANALYZE_PUBLIC_DATA = "analyze_public_data"
    GENERATE_REPORT = "generate_report"
    CREATE_ASSET = "create_asset"
    COMMIT_DEV_BRANCH = "commit_dev_branch"

    # Restricted actions (require human approval)
    DEPLOY = "deploy"
    SPEND_MONEY = "spend_money"
    MODIFY_MONETIZATION = "modify_monetization"
    COLLECT_USER_DATA = "collect_user_data"
    EXTERNAL_PAID_API = "external_paid_api"
    PRODUCTION_CHANGE = "production_change"
    SEND_NOTIFICATION = "send_notification"
    AB_TEST_MONETIZATION = "ab_test_monetization"


class RequiresHumanApproval(Exception):
    """Raised when an action requires human approval before execution."""
    pass


@dataclass
class ActionRequest:
    """Represents a request to perform an action."""
    action_type: ActionType
    description: str
    parameters: dict = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "action_type": self.action_type.value,
            "description": self.description,
            "parameters": self.parameters,
            "timestamp": self.timestamp.isoformat()
        }


@dataclass
class ActionLog:
    """Log entry for an action."""
    request: ActionRequest
    approved: bool
    executed: bool
    result: Any = None
    error: str = None

    def to_dict(self) -> dict:
        return {
            "request": self.request.to_dict(),
            "approved": self.approved,
            "executed": self.executed,
            "result": str(self.result) if self.result else None,
            "error": self.error
        }


class ApprovalGate:
    """
    Manages approval requirements for different action types.

    Actions are categorized as either autonomous (can proceed without approval)
    or restricted (must be flagged for human review and manual execution).
    """

    # Actions that require human approval - these cannot be executed autonomously
    RESTRICTED_ACTIONS = {
        ActionType.DEPLOY,
        ActionType.SPEND_MONEY,
        ActionType.MODIFY_MONETIZATION,
        ActionType.COLLECT_USER_DATA,
        ActionType.EXTERNAL_PAID_API,
        ActionType.PRODUCTION_CHANGE,
        ActionType.SEND_NOTIFICATION,
        ActionType.AB_TEST_MONETIZATION,
    }

    def check(self, action_type: ActionType) -> bool:
        """
        Check if an action can proceed autonomously.

        Args:
            action_type: The type of action to check

        Returns:
            True if action can proceed autonomously

        Raises:
            RequiresHumanApproval: If action requires human approval
        """
        if action_type in self.RESTRICTED_ACTIONS:
            raise RequiresHumanApproval(
                f"Action '{action_type.value}' requires human approval.\n"
                f"This action cannot be executed autonomously.\n"
                f"Please review the request and execute manually if appropriate."
            )
        return True

    def is_restricted(self, action_type: ActionType) -> bool:
        """Check if an action type is restricted."""
        return action_type in self.RESTRICTED_ACTIONS


class Orchestrator:
    """
    Central control system for the Mobile Game Factory.

    Coordinates tools and enforces approval gates for restricted actions.
    All actions are logged for audit purposes.
    """

    def __init__(self):
        self.approval_gate = ApprovalGate()
        self.action_log: list[ActionLog] = []
        self.pending_approvals: list[ActionRequest] = []
        logger.info("Orchestrator initialized")

    def request_action(self, action_type: ActionType, description: str,
                       parameters: dict = None) -> ActionLog:
        """
        Request to perform an action.

        If the action is autonomous, it will be marked for execution.
        If restricted, it will be added to pending approvals for human review.

        Args:
            action_type: Type of action to perform
            description: Human-readable description of what the action does
            parameters: Action-specific parameters

        Returns:
            ActionLog entry for this request
        """
        request = ActionRequest(
            action_type=action_type,
            description=description,
            parameters=parameters or {}
        )

        logger.info(f"Action requested: {action_type.value} - {description}")

        try:
            self.approval_gate.check(action_type)
            # Action is autonomous - can proceed
            log_entry = ActionLog(
                request=request,
                approved=True,
                executed=False  # Caller must execute
            )
            logger.info(f"Action approved for autonomous execution: {action_type.value}")

        except RequiresHumanApproval as e:
            # Action requires human approval
            self.pending_approvals.append(request)
            log_entry = ActionLog(
                request=request,
                approved=False,
                executed=False,
                error=str(e)
            )
            logger.warning(f"Action requires human approval: {action_type.value}")
            print(f"\n{'='*60}")
            print(f"ACTION REQUIRES HUMAN APPROVAL")
            print(f"{'='*60}")
            print(f"Type: {action_type.value}")
            print(f"Description: {description}")
            if parameters:
                print(f"Parameters: {parameters}")
            print(f"{'='*60}\n")

        self.action_log.append(log_entry)
        return log_entry

    def get_pending_approvals(self) -> list[ActionRequest]:
        """Get all actions pending human approval."""
        return self.pending_approvals.copy()

    def get_action_log(self) -> list[dict]:
        """Get complete action log as list of dicts."""
        return [entry.to_dict() for entry in self.action_log]

    def clear_pending(self, action_request: ActionRequest):
        """Remove an action from pending approvals after human review."""
        if action_request in self.pending_approvals:
            self.pending_approvals.remove(action_request)
            logger.info(f"Cleared pending approval: {action_request.action_type.value}")

    def generate_report(self) -> str:
        """Generate a summary report of all actions."""
        total = len(self.action_log)
        approved = sum(1 for log in self.action_log if log.approved)
        pending = len(self.pending_approvals)

        report = f"""
Orchestrator Action Report
===========================
Total actions requested: {total}
Autonomous (approved): {approved}
Pending human approval: {pending}

Pending Actions:
"""
        for req in self.pending_approvals:
            report += f"  - [{req.action_type.value}] {req.description}\n"

        return report


# Convenience functions for common operations

def create_orchestrator() -> Orchestrator:
    """Create and return a new Orchestrator instance."""
    return Orchestrator()


def check_can_execute(action_type: ActionType) -> bool:
    """
    Quick check if an action type can be executed autonomously.

    Returns True if autonomous, False if requires approval.
    """
    gate = ApprovalGate()
    return not gate.is_restricted(action_type)


# Example usage
if __name__ == "__main__":
    orch = create_orchestrator()

    # This will succeed (autonomous action)
    result = orch.request_action(
        ActionType.GENERATE_CODE,
        "Generate puzzle game prototype",
        {"game_type": "block_puzzle", "levels": 20}
    )
    print(f"Generate code approved: {result.approved}")

    # This will be flagged for human approval
    result = orch.request_action(
        ActionType.DEPLOY,
        "Deploy game to Google Play Store",
        {"package": "com.example.puzzle", "track": "internal"}
    )
    print(f"Deploy approved: {result.approved}")

    # Print report
    print(orch.generate_report())
