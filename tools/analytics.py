"""
Analytics - Quality-focused game performance analysis

This system analyzes game performance metrics to improve quality and player
experience. It explicitly does NOT optimize for monetization or engagement
manipulation.

Per CONSTRAINTS.md, this system:
- Generates reports for human review
- Does not autonomously deploy changes
- Focuses on quality metrics, not revenue optimization
"""

import json
import logging
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from enum import Enum

from .orchestrator import Orchestrator, ActionType

logger = logging.getLogger('analytics')


class MetricCategory(Enum):
    """Categories of metrics we track."""
    # Allowed - Quality focused
    QUALITY = "quality"
    USABILITY = "usability"
    PERFORMANCE = "performance"
    CONTENT = "content"

    # Not allowed - Would enable manipulation
    # MONETIZATION = "monetization"  # Not tracked
    # ENGAGEMENT_OPTIMIZATION = "engagement_optimization"  # Not tracked


@dataclass
class Metric:
    """A single metric measurement."""
    name: str
    category: MetricCategory
    value: float
    unit: str
    timestamp: datetime = field(default_factory=datetime.now)
    context: dict = field(default_factory=dict)


@dataclass
class QualityInsight:
    """An insight derived from quality metrics."""
    title: str
    description: str
    metrics_used: list[str]
    recommendation: str
    priority: str  # "high", "medium", "low"
    requires_human_review: bool = True


@dataclass
class AnalyticsReport:
    """A complete analytics report for human review."""
    game_name: str
    period: str
    generated_date: datetime
    metrics_summary: dict
    insights: list[QualityInsight]
    recommended_actions: list[str]


class GameAnalytics:
    """
    Analyzes game performance for quality improvements.

    This system generates insights and recommendations for human review.
    It does not autonomously make changes to games or optimize monetization.
    """

    # Metrics we track (quality-focused)
    ALLOWED_METRICS = {
        # Quality metrics
        "crash_free_rate": MetricCategory.QUALITY,
        "load_time_seconds": MetricCategory.QUALITY,
        "frame_rate_avg": MetricCategory.QUALITY,

        # Usability metrics
        "level_completion_rate": MetricCategory.USABILITY,
        "tutorial_completion_rate": MetricCategory.USABILITY,
        "quit_points": MetricCategory.USABILITY,  # Where players stop playing
        "retry_rate": MetricCategory.USABILITY,

        # Content metrics
        "levels_played": MetricCategory.CONTENT,
        "favorite_levels": MetricCategory.CONTENT,
        "skipped_levels": MetricCategory.CONTENT,

        # Performance metrics
        "memory_usage_mb": MetricCategory.PERFORMANCE,
        "battery_drain_rate": MetricCategory.PERFORMANCE,
    }

    # Metrics we explicitly do NOT track (would enable manipulation)
    PROHIBITED_METRICS = [
        "ad_click_rate",  # Would optimize ad placement
        "purchase_conversion",  # Would optimize monetization
        "session_length_optimization",  # Would optimize for addiction
        "notification_response_rate",  # Would optimize spam
        "whale_identification",  # Would target high spenders
    ]

    def __init__(self, orchestrator: Orchestrator, data_dir: Path):
        self.orchestrator = orchestrator
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.metrics: list[Metric] = []
        logger.info(f"GameAnalytics initialized, data dir: {data_dir}")

    def record_metric(self, name: str, value: float, unit: str = "",
                     context: dict = None) -> Optional[Metric]:
        """
        Record a quality metric.

        Only allowed metrics can be recorded. Prohibited metrics will be rejected.
        """
        # Check if metric is allowed
        if name not in self.ALLOWED_METRICS:
            if name in self.PROHIBITED_METRICS:
                logger.warning(
                    f"Rejected prohibited metric: {name}. "
                    f"This metric could enable manipulation and is not tracked."
                )
                return None
            else:
                logger.warning(f"Unknown metric: {name}. Not recorded.")
                return None

        category = self.ALLOWED_METRICS[name]

        metric = Metric(
            name=name,
            category=category,
            value=value,
            unit=unit,
            context=context or {}
        )
        self.metrics.append(metric)

        logger.info(f"Recorded metric: {name} = {value} {unit}")
        return metric

    def analyze(self, game_name: str, period: str = "last_7_days") -> AnalyticsReport:
        """
        Analyze collected metrics and generate insights.

        Returns a report for human review with recommendations.
        """
        self.orchestrator.request_action(
            ActionType.GENERATE_REPORT,
            f"Generating analytics report for {game_name}",
            {"metric_count": len(self.metrics), "period": period}
        )

        # Generate metrics summary
        metrics_summary = self._summarize_metrics()

        # Generate insights
        insights = self._generate_insights(metrics_summary)

        # Generate recommended actions
        recommended_actions = self._generate_recommendations(insights)

        report = AnalyticsReport(
            game_name=game_name,
            period=period,
            generated_date=datetime.now(),
            metrics_summary=metrics_summary,
            insights=insights,
            recommended_actions=recommended_actions
        )

        # Save report for human review
        self._save_report(report)

        logger.info(f"Generated analytics report with {len(insights)} insights")
        return report

    def _summarize_metrics(self) -> dict:
        """Summarize collected metrics by category."""
        summary = {}

        for metric in self.metrics:
            cat = metric.category.value
            if cat not in summary:
                summary[cat] = {}

            if metric.name not in summary[cat]:
                summary[cat][metric.name] = []

            summary[cat][metric.name].append(metric.value)

        # Calculate averages
        for cat in summary:
            for name in summary[cat]:
                values = summary[cat][name]
                summary[cat][name] = {
                    "avg": sum(values) / len(values),
                    "min": min(values),
                    "max": max(values),
                    "count": len(values)
                }

        return summary

    def _generate_insights(self, summary: dict) -> list[QualityInsight]:
        """Generate quality insights from metrics summary."""
        insights = []

        # Check for quality issues
        if "quality" in summary:
            quality = summary["quality"]

            # Crash rate
            if "crash_free_rate" in quality:
                rate = quality["crash_free_rate"]["avg"]
                if rate < 99.0:
                    insights.append(QualityInsight(
                        title="Stability Issues Detected",
                        description=f"Crash-free rate is {rate:.1f}%, below 99% target",
                        metrics_used=["crash_free_rate"],
                        recommendation="Investigate crash logs and fix stability issues",
                        priority="high"
                    ))

            # Load time
            if "load_time_seconds" in quality:
                load_time = quality["load_time_seconds"]["avg"]
                if load_time > 3.0:
                    insights.append(QualityInsight(
                        title="Slow Load Times",
                        description=f"Average load time is {load_time:.1f}s, above 3s target",
                        metrics_used=["load_time_seconds"],
                        recommendation="Optimize asset loading and reduce initial load",
                        priority="medium"
                    ))

        # Check for usability issues
        if "usability" in summary:
            usability = summary["usability"]

            # Level completion
            if "level_completion_rate" in usability:
                rate = usability["level_completion_rate"]["avg"]
                if rate < 0.7:
                    insights.append(QualityInsight(
                        title="Low Level Completion",
                        description=f"Only {rate*100:.0f}% of started levels are completed",
                        metrics_used=["level_completion_rate"],
                        recommendation="Review difficulty curve; levels may be too hard",
                        priority="high"
                    ))

            # Tutorial completion
            if "tutorial_completion_rate" in usability:
                rate = usability["tutorial_completion_rate"]["avg"]
                if rate < 0.8:
                    insights.append(QualityInsight(
                        title="Tutorial Drop-off",
                        description=f"Only {rate*100:.0f}% complete the tutorial",
                        metrics_used=["tutorial_completion_rate"],
                        recommendation="Simplify tutorial or make it skippable",
                        priority="medium"
                    ))

        return insights

    def _generate_recommendations(self, insights: list[QualityInsight]) -> list[str]:
        """Generate actionable recommendations from insights."""
        recommendations = []

        # Sort insights by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        sorted_insights = sorted(
            insights,
            key=lambda i: priority_order.get(i.priority, 2)
        )

        for insight in sorted_insights:
            recommendations.append(
                f"[{insight.priority.upper()}] {insight.recommendation}"
            )

        if not recommendations:
            recommendations.append(
                "No critical issues detected. Continue monitoring metrics."
            )

        # Add reminder about human review
        recommendations.append(
            "\nNOTE: All changes based on these insights require human review "
            "before implementation. Do not autonomously deploy optimizations."
        )

        return recommendations

    def _save_report(self, report: AnalyticsReport):
        """Save report to disk for human review."""
        report_data = {
            "game_name": report.game_name,
            "period": report.period,
            "generated_date": report.generated_date.isoformat(),
            "metrics_summary": report.metrics_summary,
            "insights": [
                {
                    "title": i.title,
                    "description": i.description,
                    "metrics_used": i.metrics_used,
                    "recommendation": i.recommendation,
                    "priority": i.priority
                }
                for i in report.insights
            ],
            "recommended_actions": report.recommended_actions
        }

        filename = f"analytics_{report.game_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path = self.data_dir / filename
        report_path.write_text(json.dumps(report_data, indent=2))
        logger.info(f"Analytics report saved to: {report_path}")

    def get_allowed_metrics(self) -> list[str]:
        """Get list of metrics that can be tracked."""
        return list(self.ALLOWED_METRICS.keys())

    def get_prohibited_metrics(self) -> list[str]:
        """Get list of metrics that are explicitly not tracked."""
        return self.PROHIBITED_METRICS.copy()

    def explain_metric_policy(self):
        """Print explanation of metric tracking policy."""
        print("\n" + "="*60)
        print("ANALYTICS METRIC POLICY")
        print("="*60)

        print("\nALLOWED METRICS (Quality-focused):")
        for name, category in self.ALLOWED_METRICS.items():
            print(f"  - {name} ({category.value})")

        print("\nPROHIBITED METRICS (Would enable manipulation):")
        for name in self.PROHIBITED_METRICS:
            print(f"  - {name}")

        print("\n" + "="*60)
        print("All insights require human review before action.")
        print("="*60 + "\n")


# Example usage
if __name__ == "__main__":
    from .orchestrator import create_orchestrator

    orch = create_orchestrator()
    analytics = GameAnalytics(orch, Path("./analytics_data"))

    # Record some metrics
    analytics.record_metric("crash_free_rate", 98.5, "%")
    analytics.record_metric("load_time_seconds", 4.2, "s")
    analytics.record_metric("level_completion_rate", 0.65)
    analytics.record_metric("tutorial_completion_rate", 0.75)

    # Try to record prohibited metric (will be rejected)
    analytics.record_metric("ad_click_rate", 0.05)

    # Generate report
    report = analytics.analyze("Block Master")

    print(f"\nAnalytics Report: {report.game_name}")
    print(f"Insights found: {len(report.insights)}")
    print("\nRecommended Actions:")
    for action in report.recommended_actions:
        print(f"  {action}")
