# SNFsniff.com — Production SEO Implementation

---

## 1. SITE-WIDE STRUCTURED DATA (JSON-LD)

### A. Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://snfsniff.com/#organization",
  "name": "SNFsniff",
  "url": "https://snfsniff.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://snfsniff.com/assets/logo.png",
    "width": 512,
    "height": 512
  },
  "description": "A transparent data platform for skilled nursing facilities, staffing conditions, quality scores, and workplace insights.",
  "foundingDate": "2026",
  "sameAs": [
    "https://www.linkedin.com/company/snfsniff",
    "https://twitter.com/snfsniff",
    "https://www.facebook.com/snfsniff"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hello@snfsniff.com",
    "contactType": "customer support",
    "availableLanguage": "English"
  },
  "brand": {
    "@type": "Brand",
    "name": "SNFsniff",
    "url": "https://snfsniff.com"
  },
  "publishingPrinciples": "https://snfsniff.com/about#data-methodology"
}
```

### B. WebSite + SearchAction Schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://snfsniff.com/#website",
  "name": "SNFsniff",
  "url": "https://snfsniff.com",
  "publisher": {
    "@id": "https://snfsniff.com/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://snfsniff.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  },
  "inLanguage": "en-US"
}
```

### C. BreadcrumbList Schema (Templates)

**Home > State > City > Facility:**

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://snfsniff.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{STATE_NAME}}",
      "item": "https://snfsniff.com/state/{{STATE_SLUG}}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{{CITY_NAME}}",
      "item": "https://snfsniff.com/state/{{STATE_SLUG}}/{{CITY_SLUG}}"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "{{FACILITY_NAME}}",
      "item": "https://snfsniff.com/facility/{{CCN}}"
    }
  ]
}
```

**Home > Compare:**

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://snfsniff.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Compare Facilities",
      "item": "https://snfsniff.com/compare"
    }
  ]
}
```

---

## 2. PAGE-TYPE SPECIFIC SCHEMA

### A. Facility Profile Page

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["MedicalOrganization", "NursingHome", "LocalBusiness"],
      "@id": "https://snfsniff.com/facility/{{CCN}}#facility",
      "name": "{{FACILITY_NAME}}",
      "description": "{{FACILITY_NAME}} is a {{BED_COUNT}}-bed {{OWNERSHIP_TYPE}} skilled nursing facility in {{CITY}}, {{STATE}}. CMS overall rating: {{OVERALL_RATING}}/5 stars. {{TOTAL_NURSE_HOURS}} total nursing hours per resident per day.",
      "url": "https://snfsniff.com/facility/{{CCN}}",
      "telephone": "{{PHONE}}",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "{{STREET}}",
        "addressLocality": "{{CITY}}",
        "addressRegion": "{{STATE}}",
        "postalCode": "{{ZIP}}",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "{{LAT}}",
        "longitude": "{{LNG}}"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "{{OVERALL_RATING}}",
        "bestRating": "5",
        "worstRating": "1",
        "ratingCount": "{{SURVEY_COUNT}}"
      },
      "medicalSpecialty": "{{SPECIALTIES_ARRAY}}",
      "isAcceptingNewPatients": true,
      "availableService": [
        {
          "@type": "MedicalProcedure",
          "name": "Skilled Nursing Care"
        },
        {
          "@type": "MedicalProcedure",
          "name": "Rehabilitation Services"
        }
      ],
      "paymentAccepted": "{{PAYMENT_TYPES}}",
      "currenciesAccepted": "USD",
      "numberOfEmployees": {
        "@type": "QuantitativeValue",
        "value": "{{ESTIMATED_STAFF_COUNT}}"
      },
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "CMS Overall Star Rating",
          "value": "{{OVERALL_RATING}}"
        },
        {
          "@type": "PropertyValue",
          "name": "CMS Health Inspection Rating",
          "value": "{{HEALTH_INSPECTION_RATING}}"
        },
        {
          "@type": "PropertyValue",
          "name": "CMS Staffing Rating",
          "value": "{{STAFFING_RATING}}"
        },
        {
          "@type": "PropertyValue",
          "name": "CMS Quality Measure Rating",
          "value": "{{QM_RATING}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Total Nurse Staffing Hours per Resident per Day",
          "value": "{{TOTAL_NURSE_HOURS}}"
        },
        {
          "@type": "PropertyValue",
          "name": "RN Hours per Resident per Day",
          "value": "{{RN_HOURS}}"
        },
        {
          "@type": "PropertyValue",
          "name": "LPN Hours per Resident per Day",
          "value": "{{LPN_HOURS}}"
        },
        {
          "@type": "PropertyValue",
          "name": "CNA Hours per Resident per Day",
          "value": "{{CNA_HOURS}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Total Health Deficiencies",
          "value": "{{DEFICIENCY_COUNT}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Total Fines",
          "value": "{{FINE_AMOUNT}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Ownership Type",
          "value": "{{OWNERSHIP_TYPE}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Number of Certified Beds",
          "value": "{{BED_COUNT}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Accepts Medicare",
          "value": "{{ACCEPTS_MEDICARE}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Accepts Medicaid",
          "value": "{{ACCEPTS_MEDICAID}}"
        },
        {
          "@type": "PropertyValue",
          "name": "RN Turnover Rate",
          "value": "{{RN_TURNOVER}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Total Nursing Staff Turnover",
          "value": "{{TOTAL_TURNOVER}}"
        },
        {
          "@type": "PropertyValue",
          "name": "Abuse Icon",
          "value": "{{ABUSE_ICON}}"
        }
      ],
      "areaServed": {
        "@type": "City",
        "name": "{{CITY}}",
        "containedInPlace": {
          "@type": "State",
          "name": "{{STATE_FULL}}"
        }
      },
      "parentOrganization": {
        "@type": "Organization",
        "name": "{{CHAIN_NAME}}"
      },
      "dateModified": "{{LAST_CMS_UPDATE}}"
    },
    {
      "@type": "Dataset",
      "@id": "https://snfsniff.com/facility/{{CCN}}#dataset",
      "name": "{{FACILITY_NAME}} — Staffing, Quality, and Inspection Data",
      "description": "CMS-sourced data on staffing levels, quality measures, health inspection results, penalties, and complaints for {{FACILITY_NAME}} in {{CITY}}, {{STATE}}.",
      "url": "https://snfsniff.com/facility/{{CCN}}",
      "creator": {
        "@id": "https://snfsniff.com/#organization"
      },
      "license": "https://www.usa.gov/government-works",
      "isBasedOn": "https://data.cms.gov/provider-data/dataset/4pq5-n9py",
      "temporalCoverage": "{{DATA_START_DATE}}/{{DATA_END_DATE}}",
      "distribution": {
        "@type": "DataDownload",
        "encodingFormat": "text/html",
        "contentUrl": "https://snfsniff.com/facility/{{CCN}}"
      },
      "measurementTechnique": "CMS Certification and Survey Provider Enhanced Reports (CASPER)",
      "variableMeasured": [
        {
          "@type": "PropertyValue",
          "name": "Overall Star Rating",
          "unitText": "stars (1-5)"
        },
        {
          "@type": "PropertyValue",
          "name": "RN Hours per Resident per Day",
          "unitText": "hours"
        },
        {
          "@type": "PropertyValue",
          "name": "Health Deficiencies",
          "unitText": "count"
        },
        {
          "@type": "PropertyValue",
          "name": "Nursing Staff Turnover",
          "unitText": "percentage"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://snfsniff.com/facility/{{CCN}}#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the CMS star rating for {{FACILITY_NAME}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FACILITY_NAME}} has an overall CMS rating of {{OVERALL_RATING}} out of 5 stars, with a health inspection rating of {{HEALTH_INSPECTION_RATING}}, staffing rating of {{STAFFING_RATING}}, and quality measure rating of {{QM_RATING}}. Ratings are based on the most recent CMS data as of {{LAST_CMS_UPDATE}}."
          }
        },
        {
          "@type": "Question",
          "name": "How many nursing staff hours does {{FACILITY_NAME}} provide per resident?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FACILITY_NAME}} provides {{TOTAL_NURSE_HOURS}} total nursing hours per resident per day, including {{RN_HOURS}} RN hours, {{LPN_HOURS}} LPN hours, and {{CNA_HOURS}} CNA hours. The national average is approximately 3.6 total nursing hours per resident per day."
          }
        },
        {
          "@type": "Question",
          "name": "How many deficiencies does {{FACILITY_NAME}} have?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FACILITY_NAME}} had {{DEFICIENCY_COUNT}} health deficiencies in its most recent inspection cycle, along with {{COMPLAINT_COUNT}} substantiated complaints. The facility has been assessed {{FINE_COUNT}} fines totaling ${{FINE_AMOUNT}}."
          }
        },
        {
          "@type": "Question",
          "name": "Does {{FACILITY_NAME}} accept Medicare and Medicaid?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FACILITY_NAME}} {{MEDICARE_STATUS}} Medicare and {{MEDICAID_STATUS}} Medicaid. The facility has {{BED_COUNT}} certified beds and is classified as a {{OWNERSHIP_TYPE}} organization."
          }
        },
        {
          "@type": "Question",
          "name": "What is the staff turnover rate at {{FACILITY_NAME}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FACILITY_NAME}} has a total nursing staff turnover rate of {{TOTAL_TURNOVER}}% and an RN turnover rate of {{RN_TURNOVER}}%. Lower turnover generally correlates with more consistent care and better working conditions."
          }
        }
      ]
    }
  ]
}
```

### B. City Page Schema

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "CollectionPage",
      "@id": "https://snfsniff.com/state/{{STATE_SLUG}}/{{CITY_SLUG}}#page",
      "name": "Skilled Nursing Facilities in {{CITY}}, {{STATE_ABBR}} — Ratings, Staffing & Inspections",
      "description": "Compare {{FACILITY_COUNT}} skilled nursing facilities in {{CITY}}, {{STATE_FULL}}. View CMS star ratings, staffing hours, inspection deficiencies, and quality scores side by side.",
      "url": "https://snfsniff.com/state/{{STATE_SLUG}}/{{CITY_SLUG}}",
      "isPartOf": {
        "@id": "https://snfsniff.com/#website"
      },
      "about": {
        "@type": "City",
        "name": "{{CITY}}",
        "containedInPlace": {
          "@type": "State",
          "name": "{{STATE_FULL}}"
        }
      },
      "mainEntity": {
        "@type": "ItemList",
        "name": "Skilled Nursing Facilities in {{CITY}}, {{STATE_ABBR}}",
        "numberOfItems": "{{FACILITY_COUNT}}",
        "itemListOrder": "https://schema.org/ItemListOrderDescending",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "item": {
              "@type": "NursingHome",
              "name": "{{FAC_1_NAME}}",
              "url": "https://snfsniff.com/facility/{{FAC_1_CCN}}",
              "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "{{FAC_1_RATING}}",
                "bestRating": "5"
              },
              "address": {
                "@type": "PostalAddress",
                "addressLocality": "{{CITY}}",
                "addressRegion": "{{STATE_ABBR}}"
              }
            }
          },
          {
            "@type": "ListItem",
            "position": 2,
            "item": {
              "@type": "NursingHome",
              "name": "{{FAC_2_NAME}}",
              "url": "https://snfsniff.com/facility/{{FAC_2_CCN}}",
              "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "{{FAC_2_RATING}}",
                "bestRating": "5"
              }
            }
          }
        ]
      },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".city-summary", ".top-facility-callout"]
      },
      "dateModified": "{{LAST_CMS_UPDATE}}"
    },
    {
      "@type": "FAQPage",
      "@id": "https://snfsniff.com/state/{{STATE_SLUG}}/{{CITY_SLUG}}#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What are the best nursing homes in {{CITY}}, {{STATE_ABBR}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Based on CMS data, the highest-rated nursing homes in {{CITY}}, {{STATE_ABBR}} are {{TOP_3_LIST}}. Rankings are based on overall five-star ratings, health inspection results, staffing levels, and quality measures."
          }
        },
        {
          "@type": "Question",
          "name": "How many skilled nursing facilities are in {{CITY}}, {{STATE_ABBR}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "There are {{FACILITY_COUNT}} Medicare- and Medicaid-certified skilled nursing facilities in {{CITY}}, {{STATE_ABBR}}. Of these, {{FIVE_STAR_COUNT}} have a 5-star overall rating, and the average total nursing hours per resident is {{AVG_HOURS}} per day."
          }
        },
        {
          "@type": "Question",
          "name": "What is the average CMS star rating for nursing homes in {{CITY}}, {{STATE_ABBR}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The average CMS overall star rating for skilled nursing facilities in {{CITY}}, {{STATE_ABBR}} is {{AVG_RATING}} out of 5. The national average is approximately 3.3 stars."
          }
        },
        {
          "@type": "Question",
          "name": "Which nursing homes in {{CITY}} have the most nursing staff hours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The facilities with the highest total nursing hours per resident per day in {{CITY}} are {{TOP_STAFFING_LIST}}. Higher staffing hours are associated with better patient outcomes and lower rates of adverse events."
          }
        }
      ]
    }
  ]
}
```

### C. Comparison Page Schema

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://snfsniff.com/compare/{{FAC_1_CCN}}-vs-{{FAC_2_CCN}}#page",
      "name": "{{FAC_1_NAME}} vs {{FAC_2_NAME}} — Side-by-Side Comparison",
      "description": "Compare {{FAC_1_NAME}} and {{FAC_2_NAME}} on CMS star ratings, staffing hours, inspection deficiencies, quality measures, turnover rates, and more.",
      "url": "https://snfsniff.com/compare/{{FAC_1_CCN}}-vs-{{FAC_2_CCN}}",
      "isPartOf": {
        "@id": "https://snfsniff.com/#website"
      },
      "mainEntity": {
        "@type": "ItemList",
        "name": "Facility Comparison",
        "numberOfItems": 2,
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "item": {
              "@type": "NursingHome",
              "name": "{{FAC_1_NAME}}",
              "url": "https://snfsniff.com/facility/{{FAC_1_CCN}}",
              "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "{{FAC_1_RATING}}",
                "bestRating": "5"
              }
            }
          },
          {
            "@type": "ListItem",
            "position": 2,
            "item": {
              "@type": "NursingHome",
              "name": "{{FAC_2_NAME}}",
              "url": "https://snfsniff.com/facility/{{FAC_2_CCN}}",
              "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "{{FAC_2_RATING}}",
                "bestRating": "5"
              }
            }
          }
        ]
      },
      "dateModified": "{{LAST_CMS_UPDATE}}"
    },
    {
      "@type": "FAQPage",
      "@id": "https://snfsniff.com/compare/{{FAC_1_CCN}}-vs-{{FAC_2_CCN}}#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Which is better, {{FAC_1_NAME}} or {{FAC_2_NAME}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FAC_1_NAME}} has a CMS rating of {{FAC_1_RATING}}/5 with {{FAC_1_HOURS}} nursing hours per resident, while {{FAC_2_NAME}} has a rating of {{FAC_2_RATING}}/5 with {{FAC_2_HOURS}} nursing hours. {{FAC_1_NAME}} had {{FAC_1_DEFICIENCIES}} deficiencies compared to {{FAC_2_DEFICIENCIES}} for {{FAC_2_NAME}}. The best choice depends on your specific needs and priorities."
          }
        },
        {
          "@type": "Question",
          "name": "How do staffing levels compare between {{FAC_1_NAME}} and {{FAC_2_NAME}}?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "{{FAC_1_NAME}} provides {{FAC_1_HOURS}} total nursing hours per resident per day ({{FAC_1_RN}} RN, {{FAC_1_LPN}} LPN, {{FAC_1_CNA}} CNA). {{FAC_2_NAME}} provides {{FAC_2_HOURS}} total hours ({{FAC_2_RN}} RN, {{FAC_2_LPN}} LPN, {{FAC_2_CNA}} CNA). The national average is approximately 3.6 hours."
          }
        }
      ]
    },
    {
      "@type": "HowTo",
      "name": "How to Compare Skilled Nursing Facilities",
      "description": "A step-by-step guide to evaluating and comparing skilled nursing facilities using CMS data.",
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "Check CMS Star Ratings",
          "text": "Start with the overall five-star rating. Look at health inspection, staffing, and quality measure sub-ratings independently — a facility can have a high overall rating but a low inspection score."
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "Review Staffing Levels",
          "text": "Compare total nursing hours per resident per day. Look at RN hours specifically — higher RN staffing correlates with better outcomes. Check weekend staffing separately, as it often drops."
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "Examine Inspection History",
          "text": "Review the number and severity of deficiencies. Check for patterns in complaint-driven inspections. Look at whether deficiencies were corrected on revisit."
        },
        {
          "@type": "HowToStep",
          "position": 4,
          "name": "Evaluate Penalties and Fines",
          "text": "Check total fines, payment denials, and the number of penalties. A facility with recurring fines may have systemic issues."
        },
        {
          "@type": "HowToStep",
          "position": 5,
          "name": "Consider Staff Turnover",
          "text": "Lower turnover rates indicate better working conditions and more consistent care. Compare RN turnover and total nursing staff turnover against state and national averages."
        }
      ]
    }
  ]
}
```

---

## 3. FAQ SYSTEM — QUESTION BANK

### A. Nurse-Intent Questions (Workplace Research)

**Staffing & Workload:**

1. **What is a good nurse-to-patient ratio in a skilled nursing facility?**
A safe nurse-to-patient ratio in SNFs varies by state regulation and shift. Generally, 1 RN to 15–20 residents on a day shift is common, but facilities with higher CMS staffing ratings maintain closer to 1:10. CNA ratios of 1:8 or lower are associated with better outcomes. Always check the facility's reported staffing hours per resident per day, which accounts for actual coverage.

2. **How many hours per day should a nursing home have RN coverage?**
CMS requires at least one RN on duty 8 consecutive hours per day, 7 days a week, and a licensed nurse (RN or LPN) on duty 24 hours. However, the reported RN hours per resident per day is a better quality indicator. The national average is approximately 0.6 RN hours per resident per day. Facilities above 0.8 generally receive higher staffing ratings.

3. **What does total nursing hours per resident per day mean?**
Total nursing hours per resident per day is the combined time RNs, LPNs, and CNAs spend providing direct care, divided by the number of residents. It is reported by facilities to CMS via Payroll-Based Journal (PBJ) data. The national average is approximately 3.6 hours. Higher values indicate more hands-on care time per resident.

4. **How is nurse staffing measured at nursing homes?**
CMS measures staffing through Payroll-Based Journal (PBJ) data, which facilities submit quarterly. PBJ captures actual hours worked from payroll records, not self-reported estimates. CMS calculates hours per resident per day by role (RN, LPN, CNA) and uses case-mix adjustment to account for patient acuity differences between facilities.

5. **What is a normal staff turnover rate for a skilled nursing facility?**
The national average total nursing staff turnover in SNFs is approximately 50–55% annually. RN-specific turnover averages around 40–45%. Facilities with turnover below 35% are considered above average. High turnover disrupts continuity of care and often correlates with lower CMS ratings and more inspection deficiencies.

6. **Do nursing homes report weekend staffing separately?**
Yes. CMS reports total nursing staff hours per resident per day on weekends as a separate metric. Weekend staffing is typically lower than weekday staffing. Facilities that maintain consistent weekend coverage tend to have better quality outcomes and fewer adverse events during weekends and holidays.

7. **How can I find out how much a nursing home pays RNs?**
CMS cost reports include aggregate salary data by facility, which can be used to estimate hourly wages. SNFsniff derives estimated hourly pay by role (NP, RN, LPN, CNA) from these cost reports. Note that actual compensation may vary based on shift differentials, overtime, benefits, and geographic cost-of-living adjustments.

8. **What is a case-mix adjusted staffing hour?**
Case-mix adjusted staffing hours account for the acuity (medical complexity) of a facility's residents. A facility caring for sicker patients needs more staff hours to deliver the same quality of care. CMS divides reported staffing by the nursing case-mix index to produce adjusted hours, enabling fairer comparisons between facilities with different patient populations.

9. **What does the CMS staffing rating mean?**
The CMS staffing rating (1–5 stars) is based on two measures: total nursing hours per resident per day (RN + LPN + CNA combined) and RN hours per resident per day. Both are case-mix adjusted. A 5-star rating means the facility is in approximately the top 10% nationally for staffing levels relative to patient acuity.

10. **How do I compare working conditions between two nursing homes?**
Compare total nursing hours per resident per day (higher means more staff per patient), RN turnover and total turnover rates (lower is better), deficiency counts (fewer means fewer compliance problems), and CMS staffing ratings. Also check whether the facility has had abuse citations or complaints, which may indicate workplace culture issues.

**Pay & Career:**

11. **What is the average RN salary at a skilled nursing facility?**
The average RN hourly wage in SNFs ranges from $30–$45 depending on state and facility size, based on CMS cost report data. This is generally lower than hospital RN pay but may include benefits such as tuition reimbursement. Facilities with higher CMS staffing ratings tend to pay competitively to attract and retain nurses.

12. **How much do CNAs make at nursing homes?**
CNA hourly wages in SNFs typically range from $14–$22, depending on the state and facility. Urban facilities and those in high cost-of-living areas tend to pay more. CMS cost reports provide aggregate payroll data per facility, from which estimated hourly rates can be derived. Check individual facility profiles for estimates.

13. **Do nursing homes with higher ratings pay better?**
There is a moderate positive correlation. Facilities with 4- and 5-star ratings tend to offer slightly higher compensation, likely because better pay helps attract qualified staff, which improves ratings. However, the relationship is not universal — some high-rated facilities in low cost-of-living areas pay less than poorly rated facilities in expensive markets.

14. **What shifts do nursing homes typically offer?**
Most SNFs operate three shifts: day (7am–3pm), evening (3pm–11pm), and night (11pm–7am). Some facilities use 12-hour shifts. Weekend and holiday coverage is mandatory. Night and weekend shifts often carry pay differentials. CMS reports weekday and weekend staffing separately, which reveals how a facility distributes coverage.

**Environment & Culture:**

15. **How can I tell if a nursing home is a good place to work?**
Key indicators from CMS data include: low total nursing staff turnover (under 35%), low RN turnover, high staffing ratings (4–5 stars), few inspection deficiencies, no abuse citations, and no substantiated complaints. Consistent staffing across weekdays and weekends also suggests stable operations and adequate scheduling.

16. **What does a nursing home abuse icon mean on CMS records?**
The abuse icon indicates that the facility has been cited for abuse during a recent standard health survey or complaint investigation. This is a serious red flag for both potential residents and prospective employees. Abuse citations may involve physical, verbal, sexual, or mental abuse, or neglect. Check the specific deficiency details for context.

### B. Family-Intent Questions (Evaluating Care)

**Quality & Safety:**

17. **What does the CMS five-star rating mean for nursing homes?**
The CMS five-star rating is a composite score based on three categories: health inspections (weighted most heavily), staffing levels, and quality measures. A 5-star facility performs in the top tier nationally; a 1-star facility is in the bottom tier. The rating is relative — it compares facilities to each other, not against an absolute standard.

18. **How do I check a nursing home's inspection history?**
CMS publishes inspection results from the three most recent standard health surveys for each facility. Each inspection records specific deficiencies by category and severity. SNFsniff displays this data on each facility's profile page. You can also view deficiency details at Medicare.gov's Care Compare tool using the facility's CCN number.

19. **What are nursing home deficiencies?**
Deficiencies are violations of federal quality and safety standards found during state health inspections. They range from minor (no actual harm, potential for minimal harm) to severe (immediate jeopardy to resident health or safety). Common deficiency categories include infection control, medication management, resident rights, and nutrition.

20. **How many deficiencies is normal for a nursing home?**
The national average is approximately 7–8 deficiencies per standard health inspection. Facilities with 3 or fewer are generally well above average. Facilities with 15+ deficiencies are significantly below average. The severity matters as much as the count — one serious deficiency (scope/severity level G or higher) is more concerning than several minor ones.

21. **What does "immediate jeopardy" mean in a nursing home inspection?**
Immediate jeopardy (IJ) is the most serious deficiency level in CMS inspections. It means a situation exists that has caused, or is likely to cause, serious injury, harm, impairment, or death to a resident. Facilities cited for IJ face mandatory penalties and must submit a plan of correction. This is a critical red flag when evaluating a facility.

22. **How do I find out if a nursing home has been fined?**
CMS publishes penalty data for all certified nursing facilities, including the number of fines, total fine amounts, and payment denials. SNFsniff displays this data on each facility profile. Recurring or large fines (above $50,000) indicate persistent compliance failures. Some fines may be reduced or waived after appeal.

23. **What is the difference between a complaint inspection and a standard inspection?**
Standard inspections (also called recertification surveys) occur approximately every 12–15 months on a schedule. Complaint inspections are triggered by specific complaints from residents, families, or staff and can happen at any time. Deficiencies found during complaint inspections are tracked separately and may indicate issues not caught during routine surveys.

24. **How important is the quality measure rating?**
The quality measure (QM) rating reflects clinical outcomes such as falls, infections, pressure ulcers, and use of antipsychotics. It is based on data facilities submit through the MDS (Minimum Data Set). A high QM rating (4–5 stars) suggests good clinical outcomes, but QM data is partially self-reported, so it should be considered alongside inspection results.

25. **What should I look for in a nursing home for memory care?**
Look for facilities that report dementia care as a specialty service. Check the antipsychotic medication use rate (lower is generally better). Review staffing levels — memory care units require higher CNA ratios. Check for secure/locked units. Review deficiency history for citations related to resident rights and wandering prevention.

**Practical / Financial:**

26. **Does Medicare cover skilled nursing facility stays?**
Medicare Part A covers up to 100 days in a SNF per benefit period after a qualifying hospital stay of at least 3 consecutive days. Days 1–20 are fully covered. Days 21–100 require a daily coinsurance payment (approximately $204.50 in 2025). After 100 days, Medicare coverage ends. Long-term custodial care is not covered by Medicare.

27. **What is the difference between a skilled nursing facility and a nursing home?**
Functionally, most facilities serve both roles. "Skilled nursing facility" is the Medicare/Medicaid certification term for facilities providing short-term rehabilitation and medical care. "Nursing home" colloquially refers to long-term residential care. Most CMS-certified facilities provide both short-stay rehabilitation and long-stay custodial care.

28. **How do I compare nursing homes near me?**
Search by city or ZIP code on SNFsniff to see all CMS-certified facilities in your area. Compare CMS star ratings, staffing hours per resident, deficiency counts, and penalty history. Sort by the metrics most important to you. Visit top candidates in person and observe staffing levels, cleanliness, resident engagement, and staff responsiveness.

29. **What does "for-profit" vs "non-profit" nursing home mean?**
Ownership type affects how revenue is used. For-profit facilities distribute surplus to owners/shareholders; non-profit facilities reinvest surplus into operations. Research shows non-profit SNFs tend to have slightly higher staffing levels and fewer deficiencies on average, though there is wide variation within both categories.

30. **Can I see a nursing home's ownership history?**
CMS tracks ownership changes and publishes ownership data including whether a facility has changed hands in the past 12 months. Recent ownership changes can affect quality temporarily as new operators adjust. SNFsniff displays current ownership type and chain affiliation for each facility.

### C. Operator-Intent Questions (Benchmarking & Compliance)

31. **How does CMS calculate the five-star rating?**
CMS calculates the overall rating starting with the health inspection rating, then adjusting up or down based on staffing and quality measure ratings. Health inspection ratings are state-normalized. Staffing ratings use case-mix adjusted PBJ data. QM ratings use MDS-submitted clinical data. The detailed methodology is published in the CMS Five-Star Technical Users' Guide.

32. **What triggers a CMS survey for a nursing home?**
Standard recertification surveys occur every 9–15 months (average 12.9). Complaint surveys are triggered by reports from residents, families, staff, or ombudsmen. Facilities with poor histories may receive more frequent surveys. Special focus facility (SFF) designees receive surveys approximately every 6 months.

33. **What is the Special Focus Facility program?**
The CMS Special Focus Facility (SFF) program identifies nursing homes with a history of serious quality issues for increased oversight. SFF facilities receive inspections every 6 months and must demonstrate sustained improvement or face progressive enforcement, including potential termination from Medicare/Medicaid. Approximately 80 facilities are designated SFF at any time.

34. **How do I benchmark my facility against state averages?**
Compare your facility's CMS metrics against the state averages published by CMS: overall rating, health inspection rating, staffing hours by role, deficiency counts, and quality measures. SNFsniff displays state averages on each facility profile for context. Focus on metrics where your facility falls more than one standard deviation below the state mean.

35. **What are the most common nursing home deficiency categories?**
The most frequently cited deficiency categories are: infection prevention and control, food service/dietary, resident assessment, pharmacy services, quality of care, and resident rights. Infection control deficiencies increased significantly post-2020. Free-standing facilities tend to have more deficiencies than hospital-based SNF units.

36. **How is Payroll-Based Journal (PBJ) data verified?**
CMS audits PBJ submissions by comparing reported hours against the facility's payroll records. CMS also cross-references PBJ data with the number of residents (from MDS census data). Facilities that fail PBJ audits may receive reduced staffing ratings. Intentional misreporting can result in enforcement actions and penalties.

37. **What is the average occupancy rate for skilled nursing facilities?**
National SNF occupancy rates have been approximately 75–80% post-2020, down from approximately 85% pre-2020. Occupancy varies significantly by region, with urban facilities generally running higher occupancy. CMS publishes average daily resident census data, from which occupancy can be calculated using certified bed counts.

38. **How do chain-owned facilities compare to independents?**
CMS data shows chain-owned facilities have slightly lower average ratings than independent facilities, though there is substantial variation within chains. CMS publishes chain-level average ratings for overall, health inspection, staffing, and QM categories. Large chains can be benchmarked against their own system-wide averages.

### D. General / Cross-Intent Questions

39. **Where does SNFsniff get its data?**
All data on SNFsniff comes from the Centers for Medicare & Medicaid Services (CMS). Primary sources include the Nursing Home Compare provider information dataset, Payroll-Based Journal staffing data, health inspection and deficiency reports, quality measure data from MDS submissions, penalty records, and cost reports. Data is public domain under federal open data policy.

40. **How often is SNFsniff data updated?**
CMS releases updated nursing home data monthly. SNFsniff processes and publishes updated data following each CMS release. Star ratings, staffing hours, deficiency counts, and quality measures reflect the most recent CMS publication date, which is displayed on each facility profile.

41. **What is the Nursing Home Compare dataset?**
Nursing Home Compare is a CMS dataset containing quality and operational data for approximately 15,000 Medicare- and Medicaid-certified nursing facilities in the United States. It includes star ratings, inspection results, staffing levels, quality measures, ownership information, and penalty history. It is the primary data source for SNFsniff.

42. **Can I download SNFsniff data?**
The underlying data is publicly available from CMS at data.cms.gov. SNFsniff presents this data in a more accessible format with additional derived metrics such as estimated hourly wages and comparative rankings. The original CMS datasets are available for download in CSV format.

43. **How accurate are CMS nursing home ratings?**
CMS ratings are based on standardized data collection and methodology, but have known limitations. Health inspection ratings depend on surveyor judgment and vary by state. Staffing data relies on PBJ submissions that can contain reporting errors. Quality measures are partially self-reported. The ratings are the best available standardized comparison tool but should not be the sole basis for decisions.

44. **What does "provider resides in hospital" mean?**
This indicates the SNF unit is located within or attached to a hospital, as opposed to being a free-standing nursing facility. Hospital-based SNF units tend to have higher staffing levels and fewer deficiencies on average, partly because they can share resources with the hospital. They also tend to focus more on short-stay rehabilitation.

45. **What is a continuing care retirement community (CCRC)?**
A CCRC offers multiple levels of care — independent living, assisted living, and skilled nursing — on a single campus. Residents can transition between levels as their needs change. CMS flags facilities that are part of a CCRC. CCRC-affiliated SNFs may have different financial and operational characteristics than stand-alone facilities.

46. **How are nursing home penalties determined?**
CMS penalties include civil money penalties (fines), denial of payment for new admissions, and ultimately termination from Medicare/Medicaid. Penalty amounts are based on deficiency severity, scope, and duration. Per-day fines range from $50–$21,395 and per-instance fines from $1,000–$71,317 (2025 figures, adjusted annually for inflation).

47. **What is the difference between long-stay and short-stay quality measures?**
Long-stay measures apply to residents who have been in the facility 100+ days and track outcomes like falls, pressure ulcers, UTIs, antipsychotic use, and physical restraints. Short-stay measures apply to residents discharged within 100 days and track rehab outcomes, readmission rates, and emergency department visits. Both are reported separately in CMS data.

48. **Can nursing home data predict future quality?**
Historical trends are moderately predictive. Facilities with declining ratings over 2–3 years, increasing deficiency counts, rising turnover, or recent ownership changes are statistically more likely to perform poorly in future inspections. However, new management or capital investment can reverse trends. Use multi-year data, not a single snapshot.

49. **What are fire safety citations and how do they differ from health citations?**
Fire safety (Life Safety Code) inspections are conducted separately from health inspections and evaluate compliance with fire safety standards: sprinkler systems, smoke detectors, emergency exits, electrical safety, and evacuation plans. They are tracked and published separately by CMS. Serious fire safety deficiencies can result in independent penalties.

50. **How do I report a concern about a nursing home?**
Contact your state's long-term care ombudsman program (federally mandated in every state) or file a complaint with your state health department's survey agency. CMS also accepts complaints through 1-800-MEDICARE. Complaints trigger unannounced complaint investigations, and the results are published in the facility's inspection record.


---

## 4. INTERNAL LINKING & CONTENT SCALING LOGIC

### Auto-Linking Rules

**FAQ answers should link to:**
- Facility names → `/facility/{{CCN}}`
- City mentions → `/state/{{STATE_SLUG}}/{{CITY_SLUG}}`
- State mentions → `/state/{{STATE_SLUG}}`
- "Compare" verbs → `/compare`
- CMS data references → `/about#data-methodology`
- Role-specific terms (RN, CNA wages) → relevant filtered view

**Implementation:**
```
Pattern: "nursing homes in {City}, {State}"
Link to: /state/{state_slug}/{city_slug}

Pattern: "{Facility Name}" (exact match against facility index)
Link to: /facility/{ccn}

Pattern: "compare facilities" / "side by side"
Link to: /compare
```

### Duplicate Content Prevention

1. **Canonical URLs** — Every page must have `<link rel="canonical">` pointing to its definitive URL.
   - Facility: `https://snfsniff.com/facility/{CCN}`
   - City: `https://snfsniff.com/state/{state}/{city}`
   - State: `https://snfsniff.com/state/{state}`
   - Compare: `https://snfsniff.com/compare/{ccn1}-vs-{ccn2}` (always sort CCNs alphabetically so A-vs-B and B-vs-A resolve to the same canonical)

2. **Parameterized pages** — Sort/filter parameters (`?sort=rating&page=2`) should use `rel="canonical"` pointing to the base page. Add `<meta name="robots" content="noindex, follow">` for filtered/sorted variants beyond the first page if content is substantially duplicated.

3. **City vs. state overlap** — State pages should list cities with links, not duplicate the full facility cards shown on city pages. Each page must have unique title, description, and introductory content.

4. **FAQ deduplication** — Facility-specific FAQ answers must include the facility name to differentiate from generic FAQ content. Never use identical answer text across multiple pages. Template variables (`{{FACILITY_NAME}}`, `{{CITY}}`) ensure uniqueness at scale.

### Canonicalization Strategy

```html
<!-- Facility page -->
<link rel="canonical" href="https://snfsniff.com/facility/105001" />

<!-- City page -->
<link rel="canonical" href="https://snfsniff.com/state/florida/miami" />

<!-- City page, sorted -->
<link rel="canonical" href="https://snfsniff.com/state/florida/miami" />
<!-- NOT: /state/florida/miami?sort=staffing -->

<!-- Compare page (CCNs sorted alphabetically) -->
<link rel="canonical" href="https://snfsniff.com/compare/105001-vs-105023" />
```

### Pagination & Crawl Optimization

1. **City pages with many facilities:** Use `rel="next"` / `rel="prev"` for paginated views. Show 20–25 facilities per page. First page gets the canonical. Subsequent pages use `<meta name="robots" content="noindex, follow">` to pass link equity without creating thin index entries.

2. **XML sitemaps:**
   - `sitemap-facilities.xml` — All ~15,000 facility URLs, `lastmod` set to latest CMS data date
   - `sitemap-cities.xml` — All city pages (~1,300+ cities)
   - `sitemap-states.xml` — 53 state/territory pages
   - `sitemap-index.xml` — Master sitemap referencing the above
   - Limit each sitemap file to 10,000 URLs

3. **Crawl budget:** Block crawling of comparison pages with more than 3 facilities in `robots.txt` (combinatorial explosion). Only allow crawl/index for 2-facility comparisons with canonicalized URLs.

```
# robots.txt
User-agent: *
Allow: /
Sitemap: https://snfsniff.com/sitemap-index.xml

# Block non-canonical comparison permutations
Disallow: /compare/*-vs-*-vs-*-vs-*
```

4. **Internal link hierarchy:**
   - Homepage links to all 53 state pages
   - State pages link to all city pages within that state
   - City pages link to all facility pages within that city
   - Facility pages link back to their city and state
   - Facility pages cross-link to "nearby facilities" (same city, max 5)
   - Comparison pages link to both facility profiles

---

## 5. CONTENT QUALITY & GOOGLE E-E-A-T

### Author Schema Strategy

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://snfsniff.com/team/medical-reviewer#person",
  "name": "{{REVIEWER_NAME}}",
  "jobTitle": "Clinical Content Reviewer",
  "description": "{{CREDENTIALS_AND_BIO}}",
  "alumniOf": "{{INSTITUTION}}",
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "credentialCategory": "{{LICENSE_TYPE}}",
      "recognizedBy": {
        "@type": "Organization",
        "name": "{{LICENSING_BODY}}"
      }
    }
  ],
  "worksFor": {
    "@id": "https://snfsniff.com/#organization"
  }
}
```

**Recommended reviewers:**
- **Medical Reviewer:** Licensed RN or NP with SNF experience. Reviews clinical content (quality measures, staffing interpretations, care-related FAQs). Byline on relevant pages.
- **Data Analyst:** Reviews data methodology content, ensures statistical claims are accurate. Byline on methodology page and data-driven content.

**Implementation:**
- Every facility profile footer: "Data sourced from CMS. Clinical context reviewed by {{REVIEWER_NAME}}, {{CREDENTIALS}}."
- FAQ pages: "Medically reviewed by {{REVIEWER_NAME}}" with link to reviewer bio.
- About page: Full bios with credentials, licensing, and professional background.

### Disclaimer Language

Place on every page in a visible footer or sidebar:

```
DISCLAIMER: SNFsniff provides publicly available data from the Centers for Medicare
& Medicaid Services (CMS) for informational purposes only. This information does not
constitute medical advice, healthcare recommendations, or endorsement of any facility.
CMS data is updated periodically and may not reflect current conditions. Always visit
facilities in person, consult with healthcare professionals, and contact facilities
directly before making care decisions. SNFsniff is not affiliated with or endorsed by
CMS or any government agency.
```

### Update Frequency Signals

- Display `dateModified` in schema on every page, matching the CMS data release date
- Show "Data last updated: {{DATE}}" visibly on facility profiles
- Use `<meta property="article:modified_time">` on content pages
- Update XML sitemap `lastmod` values with each CMS data refresh
- Maintain a changelog/data update log at `/data-updates`

### Trust Indicators

1. **Source attribution:** Every data point links to or references the specific CMS dataset
2. **Methodology page:** `/about#data-methodology` explaining exactly how data is sourced, processed, and presented
3. **No editorializing:** Present CMS data as-is without subjective rankings or "best of" claims that aren't backed by the data
4. **Transparent limitations:** Acknowledge CMS data limitations (self-reported staffing, surveyor variability) on the methodology page
5. **Government data source:** Prominently state "All data sourced from CMS.gov" — federal government data carries inherent trust
6. **HTTPS + security headers:** Required baseline for YMYL content
7. **Contact information:** Real email, physical address if possible
8. **Regular updates:** Demonstrate ongoing maintenance, not a static data dump


---

## 6. IMPLEMENTATION NOTES

### Title Tag Templates

```
Facility:  {{FACILITY_NAME}} — Ratings, Staffing & Inspections | SNFsniff
City:      Skilled Nursing Facilities in {{CITY}}, {{STATE}} | SNFsniff
State:     Nursing Homes in {{STATE_FULL}} — {{COUNT}} Facilities | SNFsniff
Compare:   {{FAC_1}} vs {{FAC_2}} — Side-by-Side Comparison | SNFsniff
Home:      SNFsniff — Compare Skilled Nursing Facilities Nationwide
```

### Meta Description Templates

```
Facility:  {{FACILITY_NAME}} in {{CITY}}, {{STATE}}: {{RATING}}-star CMS rating,
           {{HOURS}} nursing hrs/resident/day, {{DEFICIENCIES}} deficiencies.
           Compare staffing, inspections & quality.

City:      Compare {{COUNT}} skilled nursing facilities in {{CITY}}, {{STATE}}.
           CMS star ratings, staffing levels, inspection results & quality
           scores side by side.

State:     Browse {{COUNT}} nursing homes across {{STATE_FULL}}. Filter by CMS
           rating, staffing hours, deficiencies & location. Updated monthly
           from CMS data.

Compare:   {{FAC_1}} ({{R1}}★) vs {{FAC_2}} ({{R2}}★): staffing hours,
           deficiencies, quality measures & turnover compared side by side.
```

### Open Graph / Social Tags (Template)

```html
<meta property="og:type" content="website" />
<meta property="og:site_name" content="SNFsniff" />
<meta property="og:title" content="{{PAGE_TITLE}}" />
<meta property="og:description" content="{{META_DESCRIPTION}}" />
<meta property="og:url" content="{{CANONICAL_URL}}" />
<meta property="og:image" content="https://snfsniff.com/og/{{PAGE_TYPE}}-{{ID}}.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@snfsniff" />
```

### HTML FAQ Markup Structure

```html
<section class="faq-section" itemscope itemtype="https://schema.org/FAQPage">
  <h2>Frequently Asked Questions</h2>

  <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <h3 itemprop="name">{{QUESTION}}</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <div itemprop="text">
        <p>{{ANSWER}}</p>
      </div>
    </div>
  </div>

  <!-- Repeat for each FAQ -->
</section>
```

### CMS Data Model for FAQ System

```
Table: faqs
  - id (PK)
  - question (text)
  - answer (text, supports HTML)
  - intent_category (enum: nurse, family, operator, general)
  - scope (enum: global, state, city, facility)
  - priority (int, for ordering)
  - created_at
  - updated_at

Table: faq_page_assignments
  - id (PK)
  - faq_id (FK → faqs)
  - page_type (enum: facility, city, state, compare, home)
  - page_identifier (nullable, e.g. CCN, city_slug, state_slug)
  - position (int)

Table: faq_template_vars
  - id (PK)
  - faq_id (FK → faqs)
  - variable_name (e.g. "FACILITY_NAME", "OVERALL_RATING")
  - source_field (maps to CMS data column)
```

**Assignment rules:**
- Global FAQs (scope=global) can appear on any page
- Facility FAQs use template variables populated from facility data
- City FAQs use city-level aggregates
- Each page renders max 5–8 FAQs to avoid content bloat
- Priority field determines which FAQs appear when there are more candidates than slots
- Never show the same FAQ on both a city page and a facility page within that city — use scope to differentiate

### Pitfalls to Avoid

1. **Do not fabricate ratings or reviews.** `AggregateRating` must reflect actual CMS data, not user reviews you don't collect. Use `ratingCount` to reflect the number of survey cycles, not a fictitious review count.

2. **Do not use `Review` schema** unless you collect actual user reviews. Google penalizes misuse of review markup on pages without genuine reviews.

3. **Do not duplicate FAQ content** across facility and city pages. Each FAQ answer must include enough page-specific variables to be unique.

4. **Do not over-optimize comparison pages.** The combinatorial explosion of N-choose-2 comparisons across 15,000 facilities creates millions of potential pages. Only generate and index comparison pages that receive organic search demand (track via Search Console) or that are linked from facility/city pages.

5. **Avoid thin city pages.** Cities with fewer than 3 facilities should not get their own page — fold them into the state page. Set a minimum content threshold.

6. **YMYL compliance.** This is Your Money or Your Life content. Google holds healthcare content to higher E-E-A-T standards. Never make claims not supported by the data. Always include disclaimers. Always cite CMS as the source.

7. **Schema validation.** Test all JSON-LD blocks with Google's Rich Results Test and Schema.org validator before deployment. Invalid schema is worse than no schema — it can trigger manual actions.

8. **Avoid keyword stuffing in schema.** The `description` fields in schema should be natural, factual sentences — not keyword-packed strings. Google can demote sites that abuse schema for keyword insertion.

9. **Monitor for soft 404s.** If a facility loses CMS certification and is removed from the dataset, return a proper 404 or 410 status code. Do not serve an empty page with a 200 status — this creates a soft 404 that wastes crawl budget.

10. **hreflang is unnecessary** unless you plan a Spanish-language version (potentially valuable given demographics). If you do, implement `hreflang` tags on every page pair.
