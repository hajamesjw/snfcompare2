#!/usr/bin/env python3
"""
Generate SNF Compare newsletter article pages and articles index.
Outputs to deploy/articles/ directory.
"""

import os
from textwrap import dedent

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy", "articles")

# ─── Article Data ────────────────────────────────────────────────────────────

ARTICLES = [
    {
        "slug": "cms-finalizes-2026-snf-payment-rule",
        "title": "CMS Finalizes 2026 SNF Payment Rule With 3.7% Rate Increase",
        "date": "January 24, 2026",
        "date_short": "Jan 24, 2026",
        "category": "Reimbursement",
        "read_time": "5 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "The final rule updates the Patient Driven Payment Model and adjusts wage index calculations, impacting Medicare reimbursement for thousands of facilities nationwide.",
        "body": """
            <p>The Centers for Medicare &amp; Medicaid Services (CMS) has released its final rule for fiscal year 2026 skilled nursing facility (SNF) reimbursement, delivering a net 3.7% increase in Medicare payments. The rule, published in the Federal Register on January 22, represents the largest single-year rate increase for the sector since the transition to the Patient Driven Payment Model (PDPM) in 2019.</p>

            <h2>What the Rule Changes</h2>
            <p>At the heart of the update is a 2.8% market basket increase, reflecting rising costs for labor, supplies, and capital expenses. CMS applied an additional 0.9% adjustment tied to updated wage index calculations that more accurately reflect geographic labor market conditions. Together, these adjustments translate to an estimated $1.4 billion in additional Medicare spending on SNF services in FY2026.</p>
            <p>The rule also introduces refinements to the PDPM case-mix classification system. CMS has recalibrated several nursing and therapy component weights based on updated utilization data, addressing long-standing industry concerns that certain patient categories were systematically under-resourced. Facilities treating medically complex patients with high nursing needs stand to benefit the most from these adjustments.</p>

            <h2>Wage Index Overhaul</h2>
            <p>Perhaps the most consequential change is the wage index methodology update. CMS adopted a blended approach that incorporates both hospital and SNF-specific labor data, moving away from the pure hospital-based wage index that the industry has long argued fails to capture the unique labor costs of post-acute care settings. Rural facilities and those in mid-tier metropolitan areas are projected to see the largest relative gains.</p>
            <p>The American Health Care Association (AHCA) called the wage index reform &ldquo;a meaningful step toward equity&rdquo; but noted that many facilities, particularly those in high-cost urban markets, will still face significant margin pressure. According to AHCA&rsquo;s analysis, approximately 60% of SNFs operated at a loss or break-even on Medicare patients in 2025.</p>

            <h2>Industry Reaction</h2>
            <p>Operator responses have been mixed. Large multi-facility chains with diversified payer mixes are generally optimistic, viewing the rate increase as a stabilizing force. Mid-size and single-facility operators, however, express concern that the increase may not keep pace with wage inflation, particularly in states where minimum wage increases have outpaced national averages.</p>
            <p>&ldquo;A 3.7% increase sounds substantial until you factor in the 5-6% wage growth we&rsquo;re seeing in competitive labor markets,&rdquo; said one Midwest-based operator who requested anonymity. &ldquo;It&rsquo;s better than flat, but it doesn&rsquo;t close the gap.&rdquo;</p>

            <h2>What Comes Next</h2>
            <p>The rule takes effect October 1, 2026, at the start of the federal fiscal year. CMS has also signaled that it will release a proposed rule for FY2027 in the spring that may include further PDPM recalibrations and new quality reporting requirements tied to the SNF Value-Based Purchasing (VBP) program.</p>
            <p>For administrators and financial teams, the immediate priority is modeling the impact of the new rates on their specific patient mix and geographic market. Facilities with strong PDPM coding practices and a high proportion of medically complex admissions are best positioned to capitalize on the updated payment weights.</p>
        """,
        "related": ["federal-staffing-mandate-deadline", "three-states-medicaid-rate-increases", "southeast-chain-acquisition"],
    },
    {
        "slug": "federal-staffing-mandate-deadline",
        "title": "Federal Staffing Mandate Implementation Deadline Approaches: What Operators Need to Know",
        "date": "January 22, 2026",
        "date_short": "Jan 22, 2026",
        "category": "Staffing",
        "read_time": "4 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "Facilities face May 2026 compliance deadline for minimum RN and nurse aide hours per resident day requirements.",
        "body": """
            <p>With fewer than four months remaining until the May 1, 2026 compliance deadline, skilled nursing facilities across the country are scrambling to meet the federal government&rsquo;s first-ever minimum staffing requirements. The mandate, finalized by CMS in late 2024 after years of advocacy by patient safety groups, establishes minimum hours per resident day (HPRD) for registered nurses and nurse aides in all Medicare- and Medicaid-certified nursing homes.</p>

            <h2>The Requirements</h2>
            <p>Under the final rule, facilities must maintain a minimum of 0.55 RN hours per resident day (HPRD) and 2.45 nurse aide HPRD, for a combined minimum of 3.48 total nursing HPRD. Additionally, facilities must have an RN on-site 24 hours per day, seven days per week&mdash;eliminating the previous allowance for charge nurses to substitute during certain shifts.</p>
            <p>CMS estimates that approximately 75% of nursing homes will need to increase staffing levels to meet the new minimums, with rural facilities and those in states with historically low Medicaid reimbursement rates facing the steepest climb.</p>

            <h2>Compliance Challenges</h2>
            <p>The biggest barrier remains workforce availability. Despite a gradual recovery in healthcare employment since the pandemic, the nursing home sector still employs roughly 210,000 fewer workers than it did in February 2020, according to Bureau of Labor Statistics data. Certified nursing assistant (CNA) recruitment has been particularly difficult, with facilities competing against hospitals, home health agencies, and retail and hospitality employers offering comparable wages with fewer physical demands.</p>
            <p>Several state healthcare associations have filed formal comments urging CMS to extend the deadline or phase in the requirements more gradually. A coalition of operators from Texas, Louisiana, and Mississippi has argued that strict enforcement could force facility closures in underserved areas where the labor pool simply cannot support the mandated staffing levels.</p>

            <h2>Enforcement and Penalties</h2>
            <p>CMS has indicated it will use Payroll-Based Journal (PBJ) data as the primary enforcement mechanism, cross-referencing reported staffing hours with resident census data during each quarterly reporting period. Facilities found to be in persistent non-compliance will face escalating civil monetary penalties, starting at $500 per day and increasing for repeat violations.</p>
            <p>Notably, CMS has built in a hardship exemption process for facilities in rural or underserved areas that can demonstrate &ldquo;good faith efforts&rdquo; to recruit and retain staff. However, the criteria for qualifying remain vague, and industry groups have called for greater specificity.</p>

            <h2>Preparing for Compliance</h2>
            <p>Operators are pursuing multiple strategies to close staffing gaps before the deadline. These include signing bonuses and wage increases for CNAs and RNs, partnerships with local nursing schools for clinical rotations and hire pipelines, expanded use of staffing agencies (despite the premium cost), and investment in retention programs including flexible scheduling and career development pathways.</p>
            <p>For facilities that cannot meet the staffing floors by May, the most important step is documenting all recruitment and retention efforts, which will be critical for any hardship exemption application.</p>
        """,
        "related": ["cms-finalizes-2026-snf-payment-rule", "oig-infection-control-gaps", "three-states-medicaid-rate-increases"],
    },
    {
        "slug": "oig-infection-control-gaps",
        "title": "OIG Report Flags Infection Control Gaps in 30% of Surveyed Facilities",
        "date": "January 20, 2026",
        "date_short": "Jan 20, 2026",
        "category": "Operations",
        "read_time": "3 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "New oversight report calls for stricter enforcement and targeted training programs to address recurring deficiencies.",
        "body": """
            <p>A new report from the Department of Health and Human Services Office of Inspector General (OIG) has found that nearly one-third of skilled nursing facilities surveyed in 2025 had significant infection prevention and control deficiencies. The findings, based on a sample of 800 facilities across 40 states, have reignited debate over the adequacy of federal survey processes and the lingering impact of the COVID-19 pandemic on facility operations.</p>

            <h2>Key Findings</h2>
            <p>The OIG report identifies three primary areas of concern. First, 30% of surveyed facilities failed to maintain adequate hand hygiene protocols during observed care interactions. Surveyors documented instances of staff moving between residents without performing hand hygiene in 242 of 800 facilities.</p>
            <p>Second, 22% of facilities lacked current, facility-specific infection prevention and control plans (IPCPs) that addressed the full range of threats, including seasonal respiratory viruses, antibiotic-resistant organisms, and gastrointestinal outbreaks. Many plans had not been updated since the end of the federal COVID-19 Public Health Emergency in May 2023.</p>
            <p>Third, 18% of facilities had not designated a qualified infection preventionist (IP) with adequate training and dedicated time for infection control activities, as required by CMS regulations. In many cases, the IP role was assigned as an additional duty to an already overburdened director of nursing.</p>

            <h2>Recommendations</h2>
            <p>The OIG has made four formal recommendations to CMS: increase the frequency of infection control-focused surveys, develop standardized infection control training modules for surveyors, require facilities to submit annual IPCP updates as a condition of participation, and establish a public reporting mechanism for infection control deficiency trends.</p>
            <p>CMS has concurred with all four recommendations and indicated that implementation planning is underway, though no specific timeline has been provided.</p>

            <h2>Industry Response</h2>
            <p>The American Health Care Association acknowledged the findings but cautioned against a punitive approach. &ldquo;Many of the facilities flagged in this report are doing their best with limited resources,&rdquo; an AHCA spokesperson said. &ldquo;We need investment in training and staffing, not just more citations.&rdquo;</p>
            <p>Patient advocacy groups, by contrast, have seized on the report as evidence that voluntary compliance is insufficient. The Long Term Care Community Coalition called for mandatory annual infection control audits by independent assessors and publication of results on CMS&rsquo;s Care Compare website.</p>

            <h2>What Operators Should Do</h2>
            <p>Regardless of where the policy debate lands, facilities should take immediate steps to review their infection prevention programs. Priority actions include updating the facility IPCP to reflect current threats, ensuring the designated IP has adequate time and training, implementing regular hand hygiene audits with real-time feedback, and documenting all infection control training activities for survey readiness.</p>
        """,
        "related": ["federal-staffing-mandate-deadline", "states-push-back-survey-changes", "ai-fall-prevention-pilot"],
    },
    {
        "slug": "southeast-chain-acquisition",
        "title": "Major Regional Chain Acquires 45 Facilities Across Southeast",
        "date": "January 18, 2026",
        "date_short": "Jan 18, 2026",
        "category": "Finance",
        "read_time": "4 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "The $820M deal marks the largest skilled nursing acquisition in 2026, reshaping the competitive landscape in five states.",
        "body": """
            <p>In what analysts are calling the biggest skilled nursing deal in over two years, SouthCare Health Partners has completed its acquisition of 45 skilled nursing facilities across five southeastern states for approximately $820 million. The transaction, which closed on January 15 after receiving regulatory approval in all affected states, makes SouthCare the third-largest SNF operator in the Southeast with a portfolio of 112 facilities.</p>

            <h2>Deal Details</h2>
            <p>The acquired facilities, previously operated by Heritage Senior Living, span Georgia (14 facilities), Alabama (10), South Carolina (8), Tennessee (8), and Mississippi (5). The portfolio includes approximately 5,400 licensed beds and generates an estimated $480 million in annual revenue, with a payer mix of roughly 55% Medicaid, 30% Medicare, and 15% private pay and managed care.</p>
            <p>The transaction was structured as an asset purchase, with SouthCare assuming operations and retaining the majority of existing staff. Heritage Senior Living cited &ldquo;strategic realignment&rdquo; as the reason for the divestiture, though industry observers note that several of the divested facilities had experienced regulatory challenges and below-average quality ratings in recent years.</p>

            <h2>Market Impact</h2>
            <p>The acquisition reshapes the competitive landscape across the five-state region. In Georgia and Alabama, SouthCare now operates the largest number of skilled nursing beds, surpassing established regional players. The increased scale gives SouthCare greater leverage in managed care contract negotiations, group purchasing arrangements, and labor market competition.</p>
            <p>Real estate analysts value the transaction at approximately $152,000 per bed, which is in line with recent comparable transactions in the Southeast but below the $175,000-$200,000 per-bed valuations seen in higher-reimbursement states like New York and Massachusetts.</p>

            <h2>Quality Concerns</h2>
            <p>Patient advocacy groups have raised concerns about the pace of consolidation in the skilled nursing sector, noting that rapid acquisitions can disrupt care continuity. Of the 45 acquired facilities, 12 currently hold below-average quality ratings (1 or 2 stars) on CMS&rsquo;s Care Compare website.</p>
            <p>SouthCare has pledged to invest $35 million over the next 18 months in facility upgrades, technology improvements, and staffing enhancements at the acquired properties. The company says it plans to bring all facilities to at least a 3-star rating within two years.</p>

            <h2>M&amp;A Outlook</h2>
            <p>The SouthCare deal is likely a harbinger of increased M&amp;A activity in 2026. With interest rates stabilizing and several large operators signaling portfolio optimization strategies, brokers report a growing pipeline of transactions in the $50-500 million range. The Southeast and Midwest remain the most active markets, driven by favorable demographics and relatively lower per-bed valuations.</p>
            <p>For operators considering strategic alternatives, the current environment favors sellers with clean regulatory histories and diversified payer mixes. Facilities with strong Medicare Advantage relationships are particularly attractive to buyers seeking revenue predictability.</p>
        """,
        "related": ["cms-finalizes-2026-snf-payment-rule", "snf-ownership-transparency-bill", "three-states-medicaid-rate-increases"],
    },
    {
        "slug": "states-push-back-survey-changes",
        "title": "States Push Back on Federal Survey Process Changes",
        "date": "January 16, 2026",
        "date_short": "Jan 16, 2026",
        "category": "Compliance",
        "read_time": "3 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "A coalition of 12 state survey agencies raises concerns about proposed revisions to the Life Safety Code inspection framework.",
        "body": """
            <p>A coalition of 12 state survey agencies has formally pushed back against CMS&rsquo;s proposed changes to the skilled nursing facility survey process, arguing that the federal agency&rsquo;s revisions to the Life Safety Code (LSC) inspection framework would create confusion, increase costs, and potentially compromise resident safety. The joint letter, sent to CMS Administrator on January 14, represents a rare unified front among state agencies that often operate independently.</p>

            <h2>What CMS Proposed</h2>
            <p>In November 2025, CMS released proposed guidance that would overhaul the LSC survey process for long-term care facilities. Key changes include consolidating the LSC and health surveys into a single, integrated inspection event (currently conducted separately), requiring surveyors to use a new digital inspection tool that replaces existing state-specific systems, reducing the standard survey window from 15 months to 12 months between inspections, and adding new fire safety and emergency preparedness elements to the standard survey protocol.</p>
            <p>CMS argues these changes will improve efficiency, reduce burden on facilities by eliminating duplicate inspections, and create a more consistent national survey experience.</p>

            <h2>State Concerns</h2>
            <p>The 12-state coalition disagrees. Their primary concern is the mandatory adoption of CMS&rsquo;s new digital inspection tool, which they say was developed without meaningful input from state survey agencies and lacks features present in existing state systems. Several states have invested millions in custom survey management platforms over the past decade and view the federal mandate as both wasteful and technically inferior.</p>
            <p>States also raised concerns about the shortened survey window. With chronic surveyor shortages affecting nearly every state, reducing the interval from 15 to 12 months would require hiring approximately 800 additional surveyors nationwide&mdash;positions that many states cannot fund or fill in the current labor market.</p>
            <p>The coalition specifically objects to the elimination of standalone LSC surveys, arguing that fire safety inspections require specialized expertise that may be diluted in an integrated survey format. &ldquo;Life Safety Code compliance is literally a matter of life and death,&rdquo; the letter states. &ldquo;Folding it into a general health inspection risks turning it into a checkbox exercise.&rdquo;</p>

            <h2>Industry Implications</h2>
            <p>For SNF operators, the outcome of this dispute will have direct operational impact. If CMS proceeds with the integrated survey model, facilities would face a single, more intensive inspection event rather than two separate surveys. This could simplify preparation in some respects but also raises the stakes of each inspection.</p>
            <p>The shorter survey cycle would mean more frequent inspections, potentially increasing the likelihood of deficiency citations and the associated remediation burden. Operators in states with already aggressive survey schedules may see minimal change, while those in states that have historically operated at or near the 15-month maximum could face a significant adjustment.</p>

            <h2>Next Steps</h2>
            <p>CMS has a 60-day public comment period that closes in early February 2026. The agency is expected to publish a final rule by mid-2026, though the state coalition has requested a 90-day extension and a series of regional listening sessions. Given the breadth of opposition, industry observers expect CMS to modify at least some elements of the proposal before finalization.</p>
        """,
        "related": ["oig-infection-control-gaps", "federal-staffing-mandate-deadline", "snf-ownership-transparency-bill"],
    },
    {
        "slug": "ai-fall-prevention-pilot",
        "title": "AI-Powered Fall Prevention Systems Show 40% Reduction in Incidents",
        "date": "January 14, 2026",
        "date_short": "Jan 14, 2026",
        "category": "Technology",
        "read_time": "4 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "Multi-site pilot study demonstrates significant safety improvements through predictive analytics and real-time monitoring.",
        "body": """
            <p>A multi-site pilot study spanning 28 skilled nursing facilities across six states has demonstrated that AI-powered fall prevention systems can reduce fall incidents by 40% compared to traditional prevention protocols alone. The study, conducted over 12 months and published this week in the Journal of the American Medical Directors Association (JAMDA), represents the largest real-world evaluation of predictive analytics for fall prevention in long-term care settings.</p>

            <h2>How the Technology Works</h2>
            <p>The system, developed by health technology company SafeStride AI, combines three components: ambient sensor arrays installed in resident rooms and common areas that detect movement patterns and gait changes, a machine learning platform that integrates sensor data with electronic health record (EHR) information including medications, diagnoses, and recent fall history, and a real-time alert system that notifies nursing staff via mobile devices when a resident&rsquo;s fall risk exceeds a configurable threshold.</p>
            <p>Unlike camera-based monitoring systems that have faced pushback over privacy concerns, the SafeStride system uses radar and pressure sensors that detect motion patterns without capturing images. The AI component learns each resident&rsquo;s baseline movement patterns and flags deviations&mdash;such as increased nighttime restlessness, changes in walking speed, or new patterns of bed exit behavior&mdash;that research has shown to be precursors to falls.</p>

            <h2>Study Results</h2>
            <p>The 28 pilot facilities were matched with 28 control facilities of similar size, acuity mix, and baseline fall rates. Over the 12-month study period, intervention facilities experienced a 40.3% reduction in total falls and a 52% reduction in falls resulting in injury requiring medical attention. The system generated an average of 4.2 alerts per resident per month, with a clinically validated true positive rate of 73%.</p>
            <p>Nursing staff satisfaction surveys showed that 82% of direct care workers found the alert system helpful and not overly intrusive. The most commonly cited benefit was the ability to intervene proactively&mdash;for example, assisting a resident to the bathroom when the system detected increased restlessness rather than responding after a fall had already occurred.</p>

            <h2>Cost-Benefit Analysis</h2>
            <p>Fall-related injuries are among the most costly adverse events in skilled nursing, with the average fall with injury costing approximately $14,000 in direct medical expenses and liability exposure. The study estimates that participating facilities saved an average of $182,000 per year in avoided fall-related costs, against an annual technology investment of approximately $85,000 per facility. The resulting net savings of $97,000 per facility represents a return on investment that few quality improvement interventions can match.</p>

            <h2>Adoption Barriers</h2>
            <p>Despite the promising results, widespread adoption faces several hurdles. The upfront installation cost of $45,000-$65,000 per facility is prohibitive for smaller, independent operators. Integration with existing EHR systems remains technically challenging, particularly for facilities running older software platforms. Some staff and family members have expressed concerns about sensor-based monitoring, even without cameras, underscoring the need for clear communication about data use and privacy protections.</p>

            <h2>Looking Ahead</h2>
            <p>CMS has taken notice of the study and is reportedly exploring whether fall prevention technology investment could be incorporated into the SNF Value-Based Purchasing program or qualify for bonus payments under future payment models. Several state Medicaid programs are also piloting technology add-on payments that could offset adoption costs for Medicaid-heavy facilities.</p>
        """,
        "related": ["oig-infection-control-gaps", "federal-staffing-mandate-deadline", "states-push-back-survey-changes"],
    },
    {
        "slug": "three-states-medicaid-rate-increases",
        "title": "Ohio, Florida, and Pennsylvania Propose SNF Medicaid Rate Increases",
        "date": "January 12, 2026",
        "date_short": "Jan 12, 2026",
        "category": "Medicaid",
        "read_time": "3 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "Three states target chronic Medicaid underfunding with rate hikes totaling over $1.2B annually.",
        "body": """
            <p>In a sign that state-level policymakers are increasingly recognizing the financial pressures facing skilled nursing facilities, three large states&mdash;Ohio, Florida, and Pennsylvania&mdash;have included significant Medicaid rate increases for nursing homes in their proposed 2026-2027 budget plans. Together, the three proposals represent over $1.2 billion in additional annual Medicaid funding for the SNF sector.</p>

            <h2>State-by-State Breakdown</h2>
            <p><strong>Ohio</strong> has proposed a 7.5% increase in its Medicaid nursing facility per diem rate, the largest single-year increase in over a decade. The proposal, included in Governor&rsquo;s executive budget released on January 8, would raise the average daily rate from $218 to approximately $234. The increase is funded through a combination of general revenue and an enhanced provider assessment. Ohio officials cited the state&rsquo;s 14% facility closure rate since 2019 as the primary motivation.</p>
            <p><strong>Florida</strong> is proposing a 5.2% rate increase along with a new quality incentive program that would provide up to $8 per day in bonus payments for facilities meeting specified staffing and quality thresholds. The proposal aims to address Florida&rsquo;s position as one of the lowest Medicaid-reimbursing states in the country, with current rates covering an estimated 82% of the actual cost of care.</p>
            <p><strong>Pennsylvania</strong> has put forward a restructured rate methodology that would increase base rates by 4.8% while introducing a new wage pass-through component that directs a portion of the increase specifically to frontline worker compensation. The wage pass-through model requires facilities to demonstrate that at least 70% of the additional funding flows to direct care worker wages and benefits.</p>

            <h2>Why It Matters</h2>
            <p>Medicaid is the dominant payer for nursing home care, funding approximately 60% of all nursing home resident days nationwide. However, Medicaid rates have historically failed to keep pace with the actual cost of providing care, creating a structural deficit that facilities have attempted to offset with Medicare and private-pay revenue. As that cross-subsidization becomes increasingly difficult, many facilities&mdash;particularly those with high Medicaid census&mdash;face existential financial challenges.</p>
            <p>The National Health Care Association estimates that the national average Medicaid shortfall (the gap between Medicaid payment and the cost of care) reached $32.49 per resident day in 2025, totaling approximately $23.5 billion in unreimbursed costs across the sector.</p>

            <h2>Political Landscape</h2>
            <p>All three proposals face legislative hurdles. Ohio&rsquo;s increase requires approval from a state legislature that has historically been skeptical of Medicaid expansion. Florida&rsquo;s plan must navigate a budget process dominated by competing healthcare priorities, including hospital Medicaid reform and home health expansion. Pennsylvania&rsquo;s restructured methodology requires regulatory changes that some provider groups have criticized as overly prescriptive.</p>

            <h2>Implications for Operators</h2>
            <p>If enacted, these increases would provide meaningful relief for facilities in all three states. Operators should engage with state advocacy organizations to support the proposals through the legislative process and prepare for any associated reporting or quality requirements. The Pennsylvania wage pass-through model, in particular, may become a template that other states adopt, creating new compliance obligations around demonstrating how rate increases flow to worker compensation.</p>
        """,
        "related": ["cms-finalizes-2026-snf-payment-rule", "federal-staffing-mandate-deadline", "southeast-chain-acquisition"],
    },
    {
        "slug": "snf-ownership-transparency-bill",
        "title": "Bipartisan Bill Targets SNF Ownership Transparency",
        "date": "January 10, 2026",
        "date_short": "Jan 10, 2026",
        "category": "Legislation",
        "read_time": "5 min read",
        "author": "SNF Compare Editorial",
        "excerpt": "New legislation would require PE-backed operators to disclose financial structures and related-party transactions.",
        "body": """
            <p>A bipartisan group of senators has introduced the Nursing Home Ownership Transparency Act of 2026, legislation that would significantly expand disclosure requirements for skilled nursing facility ownership structures, with a particular focus on private equity-backed operators and complex multi-entity arrangements. The bill, introduced on January 8 with four co-sponsors from both parties, marks the most ambitious federal effort to date to address what advocates call the &ldquo;opacity problem&rdquo; in nursing home ownership.</p>

            <h2>What the Bill Requires</h2>
            <p>The legislation would mandate disclosure of all direct and indirect owners of nursing facilities, including private equity firms, real estate investment trusts (REITs), and management companies with ownership stakes. Current CMS requirements only capture direct owners and managing entities, leaving complex ownership chains largely opaque to regulators and the public.</p>
            <p>Specific provisions include: annual disclosure of all entities with a 5% or greater direct or indirect ownership interest (down from the current 25% threshold), mandatory reporting of all related-party transactions exceeding $10,000 annually, including management fees, real estate lease payments, and vendor contracts with affiliated entities, public disclosure of operator-level financial data aggregated across all facilities under common ownership, and a prohibition on structuring ownership arrangements primarily to shield assets from regulatory enforcement or liability claims.</p>

            <h2>The Private Equity Question</h2>
            <p>The bill emerges from growing scrutiny of private equity&rsquo;s role in the nursing home sector. Research published in leading medical journals has linked private equity ownership to increased mortality rates, higher deficiency citations, and lower staffing levels, though the industry disputes these findings and points to methodological limitations in the studies.</p>
            <p>Private equity firms have invested heavily in skilled nursing over the past decade, attracted by the sector&rsquo;s stable, government-funded revenue streams and opportunities for operational and real estate optimization. The bill&rsquo;s sponsors argue that the complex ownership structures commonly used in PE-backed acquisitions&mdash;separating real estate from operations, layering management companies and sub-entities&mdash;make it difficult for regulators to follow the money and hold responsible parties accountable.</p>

            <h2>Industry Reaction</h2>
            <p>The American Health Care Association has taken a measured stance, supporting &ldquo;reasonable transparency&rdquo; while cautioning against requirements that could create &ldquo;excessive administrative burden&rdquo; or discourage investment in the sector. AHCA has noted that many of the disclosure requirements in the bill already exist in some form at the state level, and has advocated for a federal-state harmonization approach rather than new standalone requirements.</p>
            <p>Private equity trade groups have been more critical, arguing that the bill unfairly targets one type of ownership and that its disclosure requirements could expose proprietary financial information to competitors. The American Investment Council has called the related-party transaction reporting threshold &ldquo;unworkable&rdquo; and predicts it would generate &ldquo;millions of pages of disclosures that regulators have no capacity to review.&rdquo;</p>

            <h2>Prospects for Passage</h2>
            <p>Despite bipartisan sponsorship, the bill faces an uncertain path. Similar transparency proposals have been introduced in previous congressional sessions without advancing to a vote. However, supporters point to increasing public and media attention to nursing home quality issues, a more receptive CMS leadership, and the recent release of a Government Accountability Office (GAO) report recommending enhanced ownership transparency as factors that could build momentum.</p>
            <p>Even if the full bill does not pass, individual provisions could be incorporated into must-pass legislation such as appropriations bills or Medicare/Medicaid extender packages. The related-party transaction disclosure requirement, in particular, has drawn interest from lawmakers on both sides of the aisle and could advance independently.</p>
        """,
        "related": ["southeast-chain-acquisition", "states-push-back-survey-changes", "three-states-medicaid-rate-increases"],
    },
]

# Build a lookup for article titles by slug
TITLE_BY_SLUG = {a["slug"]: a["title"] for a in ARTICLES}

# ─── HTML Templates ──────────────────────────────────────────────────────────

ARTICLE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | SNF Compare</title>
  <meta name="description" content="{excerpt}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,sans-serif; background:#fafafa; color:#1a1a1a; line-height:1.7; }}

    /* Nav */
    .article-nav {{ display:flex; align-items:center; justify-content:space-between; padding:1rem 2rem; background:#fff; border-bottom:1px solid #e5e7eb; position:sticky; top:0; z-index:100; }}
    .article-nav a {{ text-decoration:none; }}
    .nav-logo {{ display:flex; align-items:center; gap:0.5rem; font-weight:800; font-size:1.15rem; color:#0f172a; }}
    .nav-logo .badge {{ background:#10b981; color:#fff; padding:0.2rem 0.5rem; border-radius:6px; font-size:0.7rem; font-weight:700; }}
    .nav-back {{ color:#6b7280; font-size:0.88rem; font-weight:500; transition:color .2s; display:flex; align-items:center; gap:0.4rem; }}
    .nav-back:hover {{ color:#10b981; }}

    /* Article */
    .article-wrapper {{ max-width:720px; margin:0 auto; padding:3rem 1.5rem 4rem; }}
    .article-meta-top {{ display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem; flex-wrap:wrap; }}
    .category-badge {{ background:#ecfdf5; color:#059669; padding:0.3rem 0.75rem; border-radius:100px; font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; }}
    .meta-sep {{ color:#d1d5db; }}
    .meta-text {{ color:#6b7280; font-size:0.85rem; font-weight:500; }}
    .article-title {{ font-size:2.1rem; font-weight:800; color:#0f172a; line-height:1.25; letter-spacing:-0.02em; margin-bottom:1rem; }}
    .article-subtitle {{ font-size:1.1rem; color:#6b7280; line-height:1.6; margin-bottom:2rem; border-left:3px solid #10b981; padding-left:1rem; }}
    .article-byline {{ display:flex; align-items:center; gap:0.75rem; padding-bottom:2rem; border-bottom:1px solid #e5e7eb; margin-bottom:2.5rem; }}
    .byline-avatar {{ width:40px; height:40px; border-radius:50%; background:#10b981; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:0.85rem; }}
    .byline-info {{ font-size:0.85rem; }}
    .byline-name {{ font-weight:700; color:#0f172a; }}
    .byline-date {{ color:#6b7280; }}

    /* Body content */
    .article-body {{ font-size:1.05rem; color:#334155; }}
    .article-body p {{ margin-bottom:1.5rem; }}
    .article-body h2 {{ font-size:1.35rem; font-weight:800; color:#0f172a; margin:2.5rem 0 1rem; letter-spacing:-0.01em; }}
    .article-body blockquote {{ border-left:3px solid #10b981; padding:0.75rem 1.25rem; margin:1.5rem 0; background:#f0fdf4; border-radius:0 8px 8px 0; font-style:italic; color:#475569; }}
    .article-body ul, .article-body ol {{ margin:0 0 1.5rem 1.5rem; }}
    .article-body li {{ margin-bottom:0.5rem; }}

    /* Related */
    .related-section {{ margin-top:3.5rem; padding-top:2.5rem; border-top:1px solid #e5e7eb; }}
    .related-section h2 {{ font-size:1.15rem; font-weight:800; color:#0f172a; margin-bottom:1.25rem; }}
    .related-list {{ display:flex; flex-direction:column; gap:0.75rem; }}
    .related-link {{ display:block; padding:1rem 1.25rem; background:#fff; border:1px solid #e5e7eb; border-radius:12px; text-decoration:none; color:#0f172a; font-weight:600; font-size:0.95rem; transition:all .2s; }}
    .related-link:hover {{ border-color:#10b981; color:#059669; box-shadow:0 2px 8px rgba(16,185,129,.1); }}

    /* Footer */
    .article-footer {{ max-width:720px; margin:0 auto; padding:2rem 1.5rem 3rem; text-align:center; }}
    .footer-cta {{ display:inline-flex; align-items:center; gap:0.5rem; padding:0.85rem 2rem; background:#10b981; color:#fff; border-radius:100px; text-decoration:none; font-weight:700; font-size:0.95rem; transition:background .2s; margin-bottom:1.5rem; }}
    .footer-cta:hover {{ background:#059669; }}
    .footer-links {{ display:flex; justify-content:center; gap:1.5rem; margin-bottom:1rem; flex-wrap:wrap; }}
    .footer-links a {{ color:#6b7280; text-decoration:none; font-size:0.82rem; font-weight:500; transition:color .2s; }}
    .footer-links a:hover {{ color:#10b981; }}
    .footer-disclaimer {{ font-size:0.75rem; color:#9ca3af; max-width:500px; margin:0 auto; line-height:1.5; }}

    /* Responsive */
    @media (max-width:640px) {{
      .article-nav {{ padding:0.85rem 1rem; }}
      .article-wrapper {{ padding:2rem 1rem 3rem; }}
      .article-title {{ font-size:1.55rem; }}
      .article-body {{ font-size:0.98rem; }}
      .article-footer {{ padding:1.5rem 1rem 2rem; }}
    }}
  </style>
</head>
<body>
  <header class="article-nav">
    <a href="../" class="nav-logo">SNF Compare <span class="badge">NEWS</span></a>
    <a href="javascript:history.back()" class="nav-back">&larr; Back</a>
  </header>

  <article class="article-wrapper">
    <div class="article-meta-top">
      <span class="category-badge">{category}</span>
      <span class="meta-sep">&middot;</span>
      <span class="meta-text">{date}</span>
      <span class="meta-sep">&middot;</span>
      <span class="meta-text">{read_time}</span>
    </div>
    <h1 class="article-title">{title}</h1>
    <p class="article-subtitle">{excerpt}</p>
    <div class="article-byline">
      <div class="byline-avatar">SC</div>
      <div class="byline-info">
        <div class="byline-name">{author}</div>
        <div class="byline-date">{date}</div>
      </div>
    </div>
    <div class="article-body">
      {body}
    </div>
    <div class="related-section">
      <h2>Related Articles</h2>
      <div class="related-list">
        {related_html}
      </div>
    </div>
  </article>

  <footer class="article-footer">
    <a href="./" class="footer-cta">View All Articles &rarr;</a>
    <div class="footer-links">
      <a href="../">SNF Compare Tool</a>
      <a href="./">All Articles</a>
    </div>
    <p class="footer-disclaimer">SNF Compare is an independent resource. Data sourced from CMS and publicly available records. Not affiliated with or endorsed by CMS or any government agency.</p>
  </footer>
</body>
</html>
"""

INDEX_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Articles | SNF Compare News</title>
  <meta name="description" content="All SNF industry news articles — policy changes, reimbursement updates, staffing mandates, and operational insights.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,sans-serif; background:#fafafa; color:#1a1a1a; line-height:1.6; }}

    /* Nav */
    .article-nav {{ display:flex; align-items:center; justify-content:space-between; padding:1rem 2rem; background:#fff; border-bottom:1px solid #e5e7eb; position:sticky; top:0; z-index:100; }}
    .article-nav a {{ text-decoration:none; }}
    .nav-logo {{ display:flex; align-items:center; gap:0.5rem; font-weight:800; font-size:1.15rem; color:#0f172a; }}
    .nav-logo .badge {{ background:#10b981; color:#fff; padding:0.2rem 0.5rem; border-radius:6px; font-size:0.7rem; font-weight:700; }}
    .nav-back {{ color:#6b7280; font-size:0.88rem; font-weight:500; transition:color .2s; display:flex; align-items:center; gap:0.4rem; }}
    .nav-back:hover {{ color:#10b981; }}

    /* Hero */
    .index-hero {{ background:linear-gradient(135deg,#0f766e 0%,#10b981 50%,#34d399 100%); padding:3.5rem 2rem; text-align:center; color:#fff; }}
    .index-hero h1 {{ font-size:2.2rem; font-weight:800; letter-spacing:-0.02em; margin-bottom:0.5rem; }}
    .index-hero p {{ font-size:1.05rem; opacity:0.9; max-width:540px; margin:0 auto; }}

    /* Articles list */
    .index-content {{ max-width:800px; margin:0 auto; padding:2.5rem 1.5rem 4rem; }}
    .article-card {{ display:block; background:#fff; border:1px solid #e5e7eb; border-radius:16px; padding:1.75rem; margin-bottom:1rem; text-decoration:none; transition:all .2s; }}
    .article-card:hover {{ border-color:#10b981; box-shadow:0 4px 20px rgba(16,185,129,.08); transform:translateY(-1px); }}
    .card-top {{ display:flex; align-items:center; gap:0.75rem; margin-bottom:0.75rem; flex-wrap:wrap; }}
    .card-badge {{ background:#ecfdf5; color:#059669; padding:0.25rem 0.65rem; border-radius:100px; font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; }}
    .card-date {{ color:#9ca3af; font-size:0.82rem; font-weight:500; }}
    .card-title {{ font-size:1.15rem; font-weight:700; color:#0f172a; line-height:1.35; margin-bottom:0.5rem; }}
    .article-card:hover .card-title {{ color:#059669; }}
    .card-excerpt {{ font-size:0.9rem; color:#6b7280; line-height:1.55; margin-bottom:0.5rem; }}
    .card-read {{ font-size:0.82rem; color:#10b981; font-weight:600; }}

    /* Footer */
    .index-footer {{ text-align:center; padding:2rem 1.5rem 3rem; }}
    .footer-links {{ display:flex; justify-content:center; gap:1.5rem; margin-bottom:1rem; flex-wrap:wrap; }}
    .footer-links a {{ color:#6b7280; text-decoration:none; font-size:0.82rem; font-weight:500; transition:color .2s; }}
    .footer-links a:hover {{ color:#10b981; }}
    .footer-disclaimer {{ font-size:0.75rem; color:#9ca3af; max-width:500px; margin:0 auto; line-height:1.5; }}

    @media (max-width:640px) {{
      .article-nav {{ padding:0.85rem 1rem; }}
      .index-hero {{ padding:2.5rem 1rem; }}
      .index-hero h1 {{ font-size:1.65rem; }}
      .index-content {{ padding:1.5rem 1rem 3rem; }}
      .article-card {{ padding:1.25rem; }}
      .card-title {{ font-size:1.05rem; }}
    }}
  </style>
</head>
<body>
  <header class="article-nav">
    <a href="../" class="nav-logo">SNF Compare <span class="badge">NEWS</span></a>
    <a href="../" class="nav-back">&larr; Back to SNF Compare</a>
  </header>

  <div class="index-hero">
    <h1>All Articles</h1>
    <p>Policy changes, reimbursement updates, staffing mandates, and operational insights shaping the skilled nursing industry.</p>
  </div>

  <main class="index-content">
    {article_cards}
  </main>

  <footer class="index-footer">
    <div class="footer-links">
      <a href="../">SNF Compare Tool</a>
    </div>
    <p class="footer-disclaimer">SNF Compare is an independent resource. Data sourced from CMS and publicly available records. Not affiliated with or endorsed by CMS or any government agency.</p>
  </footer>
</body>
</html>
"""


def build_related_html(related_slugs):
    links = []
    for slug in related_slugs:
        title = TITLE_BY_SLUG.get(slug, slug)
        links.append(f'        <a href="{slug}.html" class="related-link">{title}</a>')
    return "\n".join(links)


def build_index_card(article):
    return f"""\
    <a href="{article['slug']}.html" class="article-card">
      <div class="card-top">
        <span class="card-badge">{article['category']}</span>
        <span class="card-date">{article['date_short']}</span>
      </div>
      <h2 class="card-title">{article['title']}</h2>
      <p class="card-excerpt">{article['excerpt']}</p>
      <span class="card-read">{article['read_time']} &rarr;</span>
    </a>"""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate individual article pages
    for article in ARTICLES:
        html = ARTICLE_TEMPLATE.format(
            title=article["title"],
            category=article["category"],
            date=article["date"],
            read_time=article["read_time"],
            author=article["author"],
            excerpt=article["excerpt"],
            body=article["body"].strip(),
            related_html=build_related_html(article["related"]),
        )
        path = os.path.join(OUTPUT_DIR, f"{article['slug']}.html")
        with open(path, "w") as f:
            f.write(html)
        print(f"  Created {path}")

    # Generate index page (articles already in reverse chronological order)
    cards = "\n".join(build_index_card(a) for a in ARTICLES)
    index_html = INDEX_TEMPLATE.format(article_cards=cards)
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w") as f:
        f.write(index_html)
    print(f"  Created {index_path}")

    print(f"\nDone! Generated {len(ARTICLES)} article pages + 1 index page in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
