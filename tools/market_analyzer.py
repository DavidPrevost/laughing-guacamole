"""
Market Analyzer - Ethical market research using legitimate data sources

This tool helps identify market opportunities using only legitimate data sources:
- Public APIs (with proper authentication)
- Published industry reports
- Manual research documentation

It does NOT scrape app stores or violate any Terms of Service.
"""

import json
import logging
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .orchestrator import Orchestrator, ActionType

logger = logging.getLogger('market_analyzer')


@dataclass
class DataSource:
    """Represents a legitimate data source."""
    name: str
    source_type: str  # "api", "report", "manual"
    url: Optional[str] = None
    requires_subscription: bool = False
    notes: str = ""


@dataclass
class MarketInsight:
    """A single market insight or finding."""
    category: str
    finding: str
    source: DataSource
    confidence: str  # "high", "medium", "low"
    date_collected: datetime = field(default_factory=datetime.now)


@dataclass
class MarketReport:
    """A complete market analysis report."""
    title: str
    generated_date: datetime
    insights: list[MarketInsight]
    opportunities: list[dict]
    recommendations: list[str]


class MarketAnalyzer:
    """
    Analyzes mobile game market using ethical data sources.

    This analyzer explicitly does NOT:
    - Scrape app stores (violates ToS)
    - Use unauthorized APIs
    - Collect non-public data

    It DOES:
    - Use public APIs with proper authentication
    - Analyze published industry reports
    - Document manual research findings
    """

    # Legitimate data sources
    LEGITIMATE_SOURCES = [
        DataSource(
            name="Sensor Tower (Public)",
            source_type="api",
            url="https://sensortower.com",
            requires_subscription=True,
            notes="Requires paid subscription for full API access"
        ),
        DataSource(
            name="Data.ai (App Annie)",
            source_type="api",
            url="https://data.ai",
            requires_subscription=True,
            notes="Requires paid subscription"
        ),
        DataSource(
            name="Newzoo Reports",
            source_type="report",
            url="https://newzoo.com",
            requires_subscription=False,
            notes="Some free reports, premium for full access"
        ),
        DataSource(
            name="GamesIndustry.biz",
            source_type="report",
            url="https://gamesindustry.biz",
            requires_subscription=False,
            notes="Free industry news and analysis"
        ),
        DataSource(
            name="Manual Research",
            source_type="manual",
            notes="Direct observation and documentation"
        ),
    ]

    def __init__(self, orchestrator: Orchestrator, data_dir: Path):
        self.orchestrator = orchestrator
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.insights: list[MarketInsight] = []
        logger.info(f"MarketAnalyzer initialized, data dir: {data_dir}")

    def add_manual_insight(self, category: str, finding: str,
                          confidence: str = "medium") -> MarketInsight:
        """
        Add a manually researched insight.

        Use this for insights gathered through legitimate means like:
        - Reading published articles
        - Analyzing games you've downloaded
        - Industry reports you have access to
        """
        self.orchestrator.request_action(
            ActionType.ANALYZE_PUBLIC_DATA,
            f"Recording manual market insight: {category}",
            {"category": category, "confidence": confidence}
        )

        insight = MarketInsight(
            category=category,
            finding=finding,
            source=DataSource(name="Manual Research", source_type="manual"),
            confidence=confidence
        )
        self.insights.append(insight)
        logger.info(f"Added manual insight: {category}")
        return insight

    def request_api_access(self, source_name: str, purpose: str) -> bool:
        """
        Request access to a paid API data source.

        This will create a pending approval for human review since
        it involves potential spending.
        """
        # This requires human approval since it may involve payment
        result = self.orchestrator.request_action(
            ActionType.EXTERNAL_PAID_API,
            f"Request access to {source_name} API for: {purpose}",
            {"source": source_name, "purpose": purpose}
        )

        # This will always return False for autonomous execution
        # Human must approve and set up the API access manually
        return result.approved

    def generate_report(self, title: str = "Market Analysis Report") -> MarketReport:
        """
        Generate a market report from collected insights.

        Returns a report with insights, opportunities, and recommendations.
        """
        self.orchestrator.request_action(
            ActionType.GENERATE_REPORT,
            f"Generating market report: {title}",
            {"insight_count": len(self.insights)}
        )

        # Analyze insights to identify opportunities
        opportunities = self._identify_opportunities()

        # Generate recommendations
        recommendations = self._generate_recommendations(opportunities)

        report = MarketReport(
            title=title,
            generated_date=datetime.now(),
            insights=self.insights,
            opportunities=opportunities,
            recommendations=recommendations
        )

        # Save report
        self._save_report(report)

        logger.info(f"Generated report with {len(opportunities)} opportunities")
        return report

    def _identify_opportunities(self) -> list[dict]:
        """Analyze insights to identify market opportunities."""
        opportunities = []

        # Group insights by category
        categories = {}
        for insight in self.insights:
            if insight.category not in categories:
                categories[insight.category] = []
            categories[insight.category].append(insight)

        # Look for patterns
        for category, category_insights in categories.items():
            if len(category_insights) >= 2:
                high_confidence = [i for i in category_insights
                                  if i.confidence == "high"]
                if high_confidence:
                    opportunities.append({
                        "category": category,
                        "insight_count": len(category_insights),
                        "confidence": "high" if len(high_confidence) > 1 else "medium",
                        "summary": f"Multiple insights support opportunity in {category}"
                    })

        return opportunities

    def _generate_recommendations(self, opportunities: list[dict]) -> list[str]:
        """Generate actionable recommendations from opportunities."""
        recommendations = []

        for opp in opportunities:
            if opp["confidence"] == "high":
                recommendations.append(
                    f"Strong opportunity in {opp['category']}: "
                    f"Consider prototyping based on {opp['insight_count']} insights"
                )
            else:
                recommendations.append(
                    f"Potential opportunity in {opp['category']}: "
                    f"Gather more data before committing resources"
                )

        if not recommendations:
            recommendations.append(
                "Insufficient data for strong recommendations. "
                "Continue gathering insights from legitimate sources."
            )

        return recommendations

    def _save_report(self, report: MarketReport):
        """Save report to disk."""
        report_data = {
            "title": report.title,
            "generated_date": report.generated_date.isoformat(),
            "insights": [
                {
                    "category": i.category,
                    "finding": i.finding,
                    "source": i.source.name,
                    "confidence": i.confidence,
                    "date": i.date_collected.isoformat()
                }
                for i in report.insights
            ],
            "opportunities": report.opportunities,
            "recommendations": report.recommendations
        }

        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path = self.data_dir / filename
        report_path.write_text(json.dumps(report_data, indent=2))
        logger.info(f"Report saved to: {report_path}")

    def get_legitimate_sources(self) -> list[DataSource]:
        """Get list of legitimate data sources."""
        return self.LEGITIMATE_SOURCES.copy()

    def print_data_source_guide(self):
        """Print guide on legitimate data sources."""
        print("\n" + "="*60)
        print("LEGITIMATE DATA SOURCES FOR MARKET RESEARCH")
        print("="*60)

        for source in self.LEGITIMATE_SOURCES:
            print(f"\n{source.name}")
            print(f"  Type: {source.source_type}")
            if source.url:
                print(f"  URL: {source.url}")
            if source.requires_subscription:
                print(f"  Note: Requires paid subscription")
            if source.notes:
                print(f"  Info: {source.notes}")

        print("\n" + "="*60)
        print("IMPORTANT: Do not scrape app stores or use unauthorized APIs")
        print("="*60 + "\n")


# Pre-defined insights based on publicly available information
# These represent general industry knowledge, not scraped data

COMMON_INDUSTRY_INSIGHTS = [
    {
        "category": "puzzle_games",
        "finding": "Hybrid-casual puzzle games combining simple mechanics with meta-progression show strong retention",
        "confidence": "high"
    },
    {
        "category": "monetization",
        "finding": "Rewarded video ads have higher user acceptance than forced interstitials",
        "confidence": "high"
    },
    {
        "category": "retention",
        "finding": "Daily challenges and streak mechanics improve D7 retention",
        "confidence": "medium"
    },
    {
        "category": "ux",
        "finding": "One-hand playability is important for mobile puzzle games",
        "confidence": "high"
    },
]


def create_analyzer_with_base_insights(orchestrator: Orchestrator,
                                       data_dir: Path) -> MarketAnalyzer:
    """Create analyzer pre-populated with common industry insights."""
    analyzer = MarketAnalyzer(orchestrator, data_dir)

    for insight_data in COMMON_INDUSTRY_INSIGHTS:
        analyzer.add_manual_insight(
            category=insight_data["category"],
            finding=insight_data["finding"],
            confidence=insight_data["confidence"]
        )

    return analyzer


# Example usage
if __name__ == "__main__":
    from .orchestrator import create_orchestrator

    orch = create_orchestrator()
    analyzer = create_analyzer_with_base_insights(orch, Path("./market_data"))

    # Add custom insight
    analyzer.add_manual_insight(
        category="mechanics",
        finding="Screw puzzle games showing 5.6x YoY growth based on industry reports",
        confidence="high"
    )

    # Generate report
    report = analyzer.generate_report("Q4 2024 Puzzle Game Market Analysis")

    print(f"\nGenerated report: {report.title}")
    print(f"Opportunities found: {len(report.opportunities)}")
    print("\nRecommendations:")
    for rec in report.recommendations:
        print(f"  - {rec}")
