#!/usr/bin/env python3
"""
generate_batch25_local.py
Generates 50 service-city pages for the 10 cities missing from 5 services.
Services: security-drivers, executive-protection, residential-security,
          event-security, close-protection-officers
Cities: atlanta, boston, chicago, houston, los-angeles, manchester,
        osaka, san-francisco, taipei, vancouver
"""
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(REPO_ROOT, "site", "content")


CITY_DATA = {
    "atlanta": {
        "city": "Atlanta", "country": "United States", "risk_level": "moderate",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Georgia Secretary of State, Professional Licensing Division",
        "license_law": "Private Detective and Security Agencies Act (OCGA Title 43, Chapter 38)",
        "license_short": "OCGA Title 43 Ch 38",
        "airport_name": "Hartsfield-Jackson Atlanta International Airport (ATL)",
        "airport_code": "ATL",
        "airport_dist": "17km south of Downtown",
        "airport_time": "25-40 minutes",
        "areas": "Buckhead, Midtown, Sandy Springs, Perimeter",
        "area1": "Buckhead", "area2": "Midtown", "area3": "Sandy Springs",
        "emergency": "911",
        "hosp1_name": "Emory University Hospital", "hosp1_tel": "404-712-2000",
        "hosp2_name": "Grady Memorial Hospital (Level 1 trauma centre)", "hosp2_tel": "404-616-1000",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "APD Crime Report 2025 records elevated carjacking and auto theft citywide, with elevated violent crime in certain Downtown areas at night",
        "crime_report": "APD Crime Report 2025",
        "key_threat": "carjacking",
        "armed_detail": "armed close protection is available through operators holding a Georgia Weapons Carry Licence and an armed security officer authorisation under OCGA Title 43 Ch 38",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 600 to 1,100 per day",
        "ep_cost": "USD 1,200 to 3,200 per day for a single-officer engagement",
        "rs_cost": "USD 3,500 to 8,000 for a property assessment; manned guarding from USD 280 to 420 per 12-hour shift",
        "es_cost": "USD 800 to 1,800 per officer per day",
        "cpo_cost": "USD 850 to 1,800 per day for a single CPO",
        "related_city1_name": "Houston", "related_city1_slug": "houston",
        "related_city2_name": "Chicago", "related_city2_slug": "chicago",
        "region": "United States",
        "event_venue": "Buckhead and Midtown venues",
        "residential_area": "Buckhead, Sandy Springs, and Perimeter",
        "police_nonemer": "Atlanta Police Department (APD), non-emergency: 404-614-6544",
    },
    "boston": {
        "city": "Boston", "country": "United States", "risk_level": "low",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Massachusetts Department of Public Safety, Licensing Division",
        "license_law": "Massachusetts Private Detective and Watch, Guard or Patrol Agency Licensing Act (MGL c.147, ss.22-30)",
        "license_short": "MGL c.147",
        "airport_name": "Boston Logan International Airport (BOS)",
        "airport_code": "BOS",
        "airport_dist": "approximately 5km from Downtown",
        "airport_time": "15-30 minutes via the Sumner or Ted Williams Tunnel",
        "areas": "Financial District, Back Bay, Seaport, Cambridge",
        "area1": "Financial District", "area2": "Back Bay", "area3": "Seaport",
        "emergency": "911",
        "hosp1_name": "Brigham and Women's Hospital", "hosp1_tel": "617-732-5500",
        "hosp2_name": "Massachusetts General Hospital", "hosp2_tel": "617-726-2000",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "BPD Crime Report 2025 records low violent crime in the Financial District, Back Bay, and Seaport; elevated crime in parts of Roxbury sits outside the standard corporate footprint",
        "crime_report": "BPD Crime Report 2025",
        "key_threat": "low ambient risk; event-security context from the 2013 Marathon bombing",
        "armed_detail": "Massachusetts has restrictive firearms licensing under MGL; armed security deployment is determined case by case against the threat assessment and is subject to restrictive state-level conditions",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 550 to 950 per day",
        "ep_cost": "USD 1,100 to 2,800 per day for a single-officer engagement",
        "rs_cost": "USD 3,000 to 7,000 for a property assessment; manned guarding from USD 260 to 400 per 12-hour shift",
        "es_cost": "USD 750 to 1,600 per officer per day",
        "cpo_cost": "USD 800 to 1,700 per day for a single CPO",
        "related_city1_name": "Chicago", "related_city1_slug": "chicago",
        "related_city2_name": "Atlanta", "related_city2_slug": "atlanta",
        "region": "United States",
        "event_venue": "Financial District, Seaport, and Cambridge conference venues",
        "residential_area": "Back Bay, Beacon Hill, and Seaport",
        "police_nonemer": "Boston Police Department (BPD), non-emergency: 617-343-4911",
    },
    "chicago": {
        "city": "Chicago", "country": "United States", "risk_level": "moderate",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Illinois Department of Financial and Professional Regulation (IDFPR)",
        "license_law": "Illinois Private Detective, Private Alarm, Private Security, Fingerprint Vendor, and Locksmith Act 2004",
        "license_short": "IDFPR Private Security Contractor licence",
        "airport_name": "O'Hare International Airport (ORD)",
        "airport_code": "ORD",
        "airport_dist": "approximately 27km north-west of the Loop",
        "airport_time": "35-50 minutes outside peak hours, up to 75 minutes during rush hour",
        "areas": "The Loop, River North, Gold Coast, Magnificent Mile",
        "area1": "The Loop", "area2": "River North", "area3": "Gold Coast",
        "emergency": "911",
        "hosp1_name": "Northwestern Memorial Hospital", "hosp1_tel": "312-926-2000",
        "hosp2_name": "Rush University Medical Center", "hosp2_tel": "312-942-5000",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "CPD Crime Report 2025 records elevated carjacking citywide and sharp neighbourhood crime disparity between the Loop and South/West Side areas",
        "crime_report": "CPD Crime Report 2025",
        "key_threat": "carjacking elevated citywide; neighbourhood crime disparity South and West Side",
        "armed_detail": "armed operators additionally require an Illinois armed contractor endorsement and a valid Firearm Owner's Identification (FOID) card under the Firearm Concealed Carry Act 2013",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 600 to 1,100 per day",
        "ep_cost": "USD 1,200 to 3,200 per day for a single-officer engagement",
        "rs_cost": "USD 3,200 to 7,500 for a property assessment; manned guarding from USD 270 to 410 per 12-hour shift",
        "es_cost": "USD 800 to 1,800 per officer per day",
        "cpo_cost": "USD 850 to 1,800 per day for a single CPO",
        "related_city1_name": "Houston", "related_city1_slug": "houston",
        "related_city2_name": "Atlanta", "related_city2_slug": "atlanta",
        "region": "United States",
        "event_venue": "McCormick Place, Navy Pier, and Loop venues",
        "residential_area": "Gold Coast, Lincoln Park, and Streeterville",
        "police_nonemer": "Chicago Police Department (CPD), non-emergency: 312-746-6000",
    },
    "houston": {
        "city": "Houston", "country": "United States", "risk_level": "moderate",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Texas Department of Public Safety (DPS), Private Security Program",
        "license_law": "Texas Private Security Act (Texas Occupations Code Chapter 1702)",
        "license_short": "Texas DPS licence under TOC Ch 1702",
        "airport_name": "George Bush Intercontinental Airport (IAH)",
        "airport_code": "IAH",
        "airport_dist": "approximately 37km north of Downtown",
        "airport_time": "40-55 minutes outside peak hours",
        "areas": "Galleria/Uptown, River Oaks, Energy Corridor, Texas Medical Center",
        "area1": "Galleria/Uptown", "area2": "River Oaks", "area3": "Energy Corridor",
        "emergency": "911",
        "hosp1_name": "Houston Methodist Hospital", "hosp1_tel": "713-790-3311",
        "hosp2_name": "Memorial Hermann-Texas Medical Center", "hosp2_tel": "713-704-4000",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "HPD Crime Report 2025 records elevated property crime and vehicle theft across the metropolitan area; energy-sector executive profiles carry specific risk considerations requiring individual assessment",
        "crime_report": "HPD Crime Report 2025",
        "key_threat": "property and vehicle crime elevated; energy-sector executive exposure",
        "armed_detail": "armed operators must hold a Texas DPS armed security officer endorsement under TOC Ch 1702; Texas has permissive firearms laws and armed deployment is assessed case by case",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 600 to 1,100 per day",
        "ep_cost": "USD 1,200 to 3,200 per day for a single-officer engagement",
        "rs_cost": "USD 3,500 to 8,000 for a property assessment; manned guarding from USD 280 to 420 per 12-hour shift",
        "es_cost": "USD 800 to 1,800 per officer per day",
        "cpo_cost": "USD 850 to 1,800 per day for a single CPO",
        "related_city1_name": "Chicago", "related_city1_slug": "chicago",
        "related_city2_name": "Atlanta", "related_city2_slug": "atlanta",
        "region": "United States",
        "event_venue": "Galleria, Downtown, and Energy Corridor venues",
        "residential_area": "River Oaks, Memorial, and West University",
        "police_nonemer": "Houston Police Department (HPD), non-emergency: 832-394-1313",
    },
    "los-angeles": {
        "city": "Los Angeles", "country": "United States", "risk_level": "moderate",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "California Bureau of Security and Investigative Services (BSIS)",
        "license_law": "California Business and Professions Code (Private Patrol Operator/PPSO licensing)",
        "license_short": "California BSIS PPO licence",
        "airport_name": "Los Angeles International Airport (LAX)",
        "airport_code": "LAX",
        "airport_dist": "approximately 27km from Beverly Hills and Downtown",
        "airport_time": "30-60 minutes, up to 90 minutes during peak-hour traffic",
        "areas": "Beverly Hills, Century City, Bel Air, Downtown Financial District",
        "area1": "Beverly Hills", "area2": "Century City", "area3": "Bel Air",
        "emergency": "911",
        "hosp1_name": "Cedars-Sinai Medical Center", "hosp1_tel": "310-423-3277",
        "hosp2_name": "UCLA Medical Center", "hosp2_tel": "310-825-9111",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "LAPD Crime Report 2025 records elevated vehicle crime and smash-and-grab incidents across the metropolitan area, with sharp neighbourhood disparity between Beverly Hills and Skid Row",
        "crime_report": "LAPD Crime Report 2025",
        "key_threat": "vehicle crime and smash-and-grab elevated; neighbourhood crime disparity",
        "armed_detail": "armed operators require a California BSIS firearms permit and a valid Guard Card; armed deployment is assessed case by case against the threat assessment",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 650 to 1,200 per day",
        "ep_cost": "USD 1,300 to 3,500 per day for a single-officer engagement",
        "rs_cost": "USD 4,000 to 9,500 for a property assessment; manned guarding from USD 300 to 450 per 12-hour shift",
        "es_cost": "USD 900 to 2,000 per officer per day",
        "cpo_cost": "USD 900 to 1,900 per day for a single CPO",
        "related_city1_name": "San Francisco", "related_city1_slug": "san-francisco",
        "related_city2_name": "Chicago", "related_city2_slug": "chicago",
        "region": "United States",
        "event_venue": "Beverly Hills, Century City, and Downtown venues",
        "residential_area": "Beverly Hills, Bel Air, and Brentwood",
        "police_nonemer": "LAPD non-emergency: 1-877-275-5273",
    },
    "manchester": {
        "city": "Manchester", "country": "United Kingdom", "risk_level": "low",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Security Industry Authority (SIA)",
        "license_law": "Private Security Industry Act 2001",
        "license_short": "SIA Close Protection licence",
        "airport_name": "Manchester Airport (MAN)",
        "airport_code": "MAN",
        "airport_dist": "approximately 14km south of the city centre",
        "airport_time": "30-40 minutes via the M56",
        "areas": "Spinningfields, Deansgate, Salford Quays, Manchester Arena",
        "area1": "Spinningfields", "area2": "Deansgate", "area3": "Salford Quays",
        "emergency": "999",
        "hosp1_name": "Manchester Royal Infirmary", "hosp1_tel": "0161-276-1234",
        "hosp2_name": "Salford Royal Hospital", "hosp2_tel": "0161-206-1234",
        "advisory_fcdo": "normal precautions for the United Kingdom (2026)",
        "advisory_sd": "Level 2 (Exercise Increased Caution) for the United Kingdom as of 2026 due to terrorism",
        "threat_note": "GMP Crime Report 2025 records low crime rates in Spinningfields, Deansgate, and Salford Quays; the UK terrorism threat level stands at SUBSTANTIAL (MI5, 2026), informed by the 2017 Manchester Arena attack",
        "crime_report": "GMP Crime Report 2025",
        "key_threat": "UK terrorism threat SUBSTANTIAL (MI5 2026); low ambient crime in corporate areas",
        "armed_detail": "UK close protection is unarmed; SIA licensing requires an approved CP qualification, first-aid certification, and enhanced criminal-record checks; armed response is a police function",
        "unarmed": True,
        "currency": "GBP",
        "sd_cost": "GBP 450 to 850 per day",
        "ep_cost": "GBP 700 to 1,600 per day for a single SIA-licensed CPO",
        "rs_cost": "GBP 2,500 to 6,000 for a property security assessment; manned guarding from GBP 180 to 320 per 12-hour shift",
        "es_cost": "GBP 500 to 1,200 per officer per day",
        "cpo_cost": "GBP 600 to 1,400 per day for a single SIA-licensed CPO",
        "related_city1_name": "London", "related_city1_slug": "london",
        "related_city2_name": "Birmingham", "related_city2_slug": "birmingham",
        "region": "United Kingdom",
        "event_venue": "Manchester Arena, Spinningfields, and Deansgate venues",
        "residential_area": "Spinningfields, Deansgate, and Salford Quays",
        "police_nonemer": "Greater Manchester Police (GMP), non-emergency: 101",
    },
    "osaka": {
        "city": "Osaka", "country": "Japan", "risk_level": "low",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "Osaka Prefectural Police (under National Public Safety Commission oversight)",
        "license_law": "Security Business Act (Act No.117 of 1972, as amended)",
        "license_short": "Security Business Act (Act No.117 of 1972)",
        "airport_name": "Kansai International Airport (KIX)",
        "airport_code": "KIX",
        "airport_dist": "approximately 50km south of the Umeda CBD",
        "airport_time": "75-90 minutes by road; 80 minutes via the Nankai Rapi:t rail service",
        "areas": "Umeda/Kita CBD, Nakanoshima, Yodoyabashi, Fukushima",
        "area1": "Umeda/Kita CBD", "area2": "Nakanoshima", "area3": "Fukushima",
        "emergency": "110 (police); 119 (fire/ambulance)",
        "hosp1_name": "Osaka University Hospital", "hosp1_tel": "06-6879-5111",
        "hosp2_name": "Osaka City General Medical Centre", "hosp2_tel": "06-6929-1221",
        "advisory_fcdo": "normal precautions for Japan (2026), with awareness of earthquake risk",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for Japan as of 2026",
        "threat_note": "NPA Crime Statistics 2024/2025 confirm very low violent crime in Osaka; petty theft in dense crowds at Dotonbori during peak tourist season is the primary residual risk",
        "crime_report": "NPA Crime Statistics 2024/2025",
        "key_threat": "very low crime; petty theft in dense Dotonbori crowds; earthquake preparedness",
        "armed_detail": "private armed close protection is not permitted in Japan; all close protection is unarmed and armed response is exclusively a police function under Japanese law",
        "unarmed": True,
        "currency": "JPY",
        "sd_cost": "JPY 60,000 to 100,000 per day",
        "ep_cost": "JPY 90,000 to 200,000 per day for a single-officer engagement",
        "rs_cost": "JPY 150,000 to 350,000 for a residential security assessment; ongoing guarding costs vary by provider and hours",
        "es_cost": "JPY 70,000 to 150,000 per officer per day",
        "cpo_cost": "JPY 80,000 to 180,000 per day for a single CPO",
        "related_city1_name": "Tokyo", "related_city1_slug": "tokyo",
        "related_city2_name": "Singapore", "related_city2_slug": "singapore",
        "region": "Japan",
        "event_venue": "Umeda and Nakanoshima conference and corporate venues",
        "residential_area": "Umeda, Fukushima, and central Osaka hotel properties",
        "police_nonemer": "Osaka Prefectural Police, emergency: 110",
    },
    "san-francisco": {
        "city": "San Francisco", "country": "United States", "risk_level": "moderate",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "California Bureau of Security and Investigative Services (BSIS)",
        "license_law": "California Business and Professions Code (Private Patrol Operator/PPSO licensing)",
        "license_short": "California BSIS PPO licence",
        "airport_name": "San Francisco International Airport (SFO)",
        "airport_code": "SFO",
        "airport_dist": "approximately 21km south of the Financial District",
        "airport_time": "30-45 minutes outside peak hours; longer during commute periods",
        "areas": "Financial District, Pacific Heights, Marina District, Mission Bay",
        "area1": "Financial District", "area2": "Pacific Heights", "area3": "Mission Bay",
        "emergency": "911",
        "hosp1_name": "Zuckerberg San Francisco General Hospital", "hosp1_tel": "415-206-8000",
        "hosp2_name": "UCSF Medical Center", "hosp2_tel": "415-476-1000",
        "advisory_fcdo": "normal precautions for the United States (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for the United States as of 2026",
        "threat_note": "SFPD Crime Report 2025 records vehicle break-in rates among the highest in California citywide, and elevated personal safety concerns in the Tenderloin and Civic Center",
        "crime_report": "SFPD Crime Report 2025",
        "key_threat": "vehicle break-ins elevated citywide; Tenderloin and Civic Center disorder",
        "armed_detail": "armed operators require a California BSIS firearms permit and a valid Guard Card; in San Francisco, local venue permitting requirements may also apply",
        "unarmed": False,
        "currency": "USD",
        "sd_cost": "USD 650 to 1,200 per day",
        "ep_cost": "USD 1,300 to 3,500 per day for a single-officer engagement",
        "rs_cost": "USD 4,000 to 10,000 for a property assessment in Pacific Heights or Marina; manned guarding from USD 310 to 460 per 12-hour shift",
        "es_cost": "USD 900 to 2,000 per officer per day",
        "cpo_cost": "USD 900 to 1,900 per day for a single CPO",
        "related_city1_name": "Los Angeles", "related_city1_slug": "los-angeles",
        "related_city2_name": "Chicago", "related_city2_slug": "chicago",
        "region": "United States",
        "event_venue": "Financial District, SoMa, and Mission Bay technology event venues",
        "residential_area": "Pacific Heights, Marina District, and Noe Valley",
        "police_nonemer": "San Francisco Police Department (SFPD), non-emergency: 415-553-0123",
    },
    "taipei": {
        "city": "Taipei", "country": "Taiwan", "risk_level": "low",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "National Police Agency (NPA), Ministry of the Interior (MOI)",
        "license_law": "Private Security Services Industry Act (2009, as amended)",
        "license_short": "Private Security Services Industry Act 2009",
        "airport_name": "Taiwan Taoyuan International Airport (TPE)",
        "airport_code": "TPE",
        "airport_dist": "approximately 40km west of Taipei city centre",
        "airport_time": "40-60 minutes by road or 35 minutes via the Airport MRT",
        "areas": "Xinyi District, Da'an District, Zhongzheng, Zhongshan",
        "area1": "Xinyi District", "area2": "Da'an District", "area3": "Zhongzheng",
        "emergency": "110 (police); 119 (fire/ambulance)",
        "hosp1_name": "National Taiwan University Hospital", "hosp1_tel": "02-2312-3456",
        "hosp2_name": "Taipei Veterans General Hospital", "hosp2_tel": "02-2871-2121",
        "advisory_fcdo": "normal precautions for Taiwan (2026), with a strategic note on cross-strait tensions for contingency planning",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for Taiwan as of 2026",
        "threat_note": "Taiwan NPA Crime Statistics 2024 confirm low violent crime in Taipei; minor petty crime in dense nightlife areas such as Ximending is the primary residual risk for corporate visitors",
        "crime_report": "Taiwan NPA Crime Statistics 2024",
        "key_threat": "very low crime; cross-strait strategic context noted for contingency planning (FCDO 2026)",
        "armed_detail": "private armed close protection is not permitted in Taiwan; all close protection is unarmed and armed response is exclusively a police function",
        "unarmed": True,
        "currency": "TWD",
        "sd_cost": "TWD 9,000 to 18,000 per day (approximately USD 280 to 560)",
        "ep_cost": "TWD 15,000 to 35,000 per day for a single-officer engagement (approximately USD 460 to 1,100)",
        "rs_cost": "TWD 40,000 to 90,000 for a residential security assessment; ongoing guarding from TWD 6,000 to 12,000 per 12-hour shift",
        "es_cost": "TWD 10,000 to 22,000 per officer per day",
        "cpo_cost": "TWD 12,000 to 28,000 per day for a single CPO",
        "related_city1_name": "Tokyo", "related_city1_slug": "tokyo",
        "related_city2_name": "Singapore", "related_city2_slug": "singapore",
        "region": "East Asia",
        "event_venue": "Xinyi CBD conference centres and Zhongshan corporate venues",
        "residential_area": "Da'an District, Zhongshan, and Xinyi",
        "police_nonemer": "Taipei City Police Department, emergency: 110",
    },
    "vancouver": {
        "city": "Vancouver", "country": "Canada", "risk_level": "low",
        "hero_image": "Close-Protection-2560.webp",
        "license_body": "BC Ministry of Public Safety and Solicitor General, Security Programs Division",
        "license_law": "BC Security Services Act 2007",
        "license_short": "BC Security Services Act 2007",
        "airport_name": "Vancouver International Airport (YVR)",
        "airport_code": "YVR",
        "airport_dist": "approximately 12km south of Downtown",
        "airport_time": "25-35 minutes via Highway 99, longer during peak commute",
        "areas": "Coal Harbour, Yaletown, West End, Robson Street",
        "area1": "Coal Harbour", "area2": "Yaletown", "area3": "West End",
        "emergency": "911",
        "hosp1_name": "Vancouver General Hospital", "hosp1_tel": "604-875-4111",
        "hosp2_name": "St. Paul's Hospital", "hosp2_tel": "604-682-2344",
        "advisory_fcdo": "normal precautions for Canada (2026)",
        "advisory_sd": "Level 1 (Exercise Normal Precautions) for Canada as of 2026",
        "threat_note": "VPD Statistical Report 2025 records low violent crime in Coal Harbour, Yaletown, and West End; the Downtown Eastside (DTES) opioid public health emergency creates elevated property crime in an area that adjoins Gastown and Chinatown",
        "crime_report": "VPD Statistical Report 2025",
        "key_threat": "Downtown Eastside property crime; vehicle break-ins in central area",
        "armed_detail": "private armed close protection is not permitted in Canada without specific federal authorisation, which is rarely granted; all close protection is effectively unarmed and armed response is a police function",
        "unarmed": True,
        "currency": "CAD",
        "sd_cost": "CAD 700 to 1,200 per day",
        "ep_cost": "CAD 900 to 2,200 per day for a single-officer engagement",
        "rs_cost": "CAD 3,500 to 8,500 for a property assessment; manned guarding from CAD 250 to 380 per 12-hour shift",
        "es_cost": "CAD 700 to 1,500 per officer per day",
        "cpo_cost": "CAD 800 to 1,800 per day for a single CPO",
        "related_city1_name": "Toronto", "related_city1_slug": "toronto",
        "related_city2_name": "Los Angeles", "related_city2_slug": "los-angeles",
        "region": "Canada",
        "event_venue": "Coal Harbour and Downtown waterfront conference venues",
        "residential_area": "Coal Harbour, West Vancouver, and Shaughnessy",
        "police_nonemer": "Vancouver Police Department (VPD), non-emergency: 604-717-3321",
    },
}


def clean(s):
    return s.replace('—', '--').replace('–', '-')


def sd_page(c):
    slug = list(k for k, v in CITY_DATA.items() if v["city"] == c["city"])[0]
    city = c["city"]
    country = c["country"]
    title = f"Security Drivers in {city}, {country}"
    if len(title) > 70:
        title = f"Security Drivers in {city}"
    seo_title = f"Security Driver {city} | Vetted {country} Transfers"
    if len(seo_title) > 70:
        seo_title = f"Security Driver {city} | Vetted Transfers"
    desc = (f"Vetted security drivers in {city}, {country}. Pre-arranged airport "
            f"transfers, route-planned movement, and operations controller cover "
            f"for corporate principals.")
    if len(desc) > 175:
        desc = desc[:172] + "..."
    if len(desc) < 120:
        desc += f" Licensed under {c['license_short']}."
    # Trim to 175
    desc = desc[:175]

    armed_str = ("Unarmed cover only; armed response is a police function in "
                 f"{country}." if c["unarmed"] else
                 f"Armed options available through operators meeting the full licensing requirement.")

    content = f"""---
title: "{clean(title)}"
description: "{clean(desc)}"
slug: "{slug}"
h1: "Security Drivers in {city}, {country}"
seo_title: "{clean(seo_title)}"
service: "security-drivers"
city: "{city}"
country: "{country}"
risk_level: "{c['risk_level']}"
hero_image: "{c['hero_image']}"
date: "2026-06-18"
cta_text: "Arriving at {c['airport_code']}? Pre-arrange your {city} secure transfer before you land."
components:
  - title: "Airport Collection Protocol: {c['airport_name']}"
    description: "{c['airport_name']} is {c['airport_dist']}, typically {c['airport_time']}. The driver is pre-positioned for terminal arrival, the vehicle is security-checked before collection, the route is pre-surveyed, and no kerbside or unlicensed transport is used."
  - title: "Route Planning and Threat Awareness"
    description: "{c['threat_note']}. Route planning incorporates current incident data to avoid predictable stopping points, high-risk junctions, and vulnerable approach roads. Counter-surveillance awareness is standard throughout all principal movements."
  - title: "Driver Vetting and Licensing"
    description: "All security drivers in {city} hold current licences under the {c['license_law']}, administered by the {c['license_body']}. Each driver passes background verification, reference checks, and operational assessment before being engaged for principal movements."
  - title: "Operations Controller Cover"
    description: "Every transfer is tracked by an operations controller from departure to drop-off. Check-ins occur at collection, mid-journey for longer routes, and on arrival. Any deviation from the planned timeline triggers an immediate welfare protocol."
  - title: "Vehicle Selection and Specification"
    description: "Vehicles are appropriate-spec, fully insured, and maintained to a standard consistent with professional close protection use. Window tint, vehicle tracking, and communications equipment are standard. For elevated-risk profiles, higher-specification vehicles are available."
  - title: "Night and Peak-Hour Protocols"
    description: "Night-time and peak-hour transfers from {c['airport_name']} require adjusted protocols: earlier accommodation liaison, confirmed hotel security contact, route selection accounting for reduced visibility and traffic patterns, and modified timing to avoid highest-risk windows."
faqs:
  - question: "Why use a security driver in {city} rather than a standard taxi?"
    answer: "{c['threat_note']}. A vetted security driver provides pre-arranged collection with no kerbside exposure, operations controller oversight, route planning based on current incident data, and driver training suited to the {city} environment. A standard taxi or ride-share service does not provide these controls."
  - question: "What licensing applies to security drivers in {country}?"
    answer: "Security drivers operating commercially in {city} must hold a current licence under the {c['license_law']}, administered by the {c['license_body']}. {armed_str} Verify any driver's licence before engagement."
  - question: "How is the {c['airport_code']} airport transfer managed?"
    answer: "{c['airport_name']} is {c['airport_dist']}. The driver is pre-positioned for the principal's arrival, the vehicle is checked before collection, and the route is pre-surveyed. Allow {c['airport_time']} and additional contingency for delays. No unlicensed kerbside transport is used."
  - question: "What does a security driver cost in {city}?"
    answer: "Security driver hire in {city} typically ranges from {c['sd_cost']} depending on vehicle specification, journey type, and whether operations controller cover is included. As at June 2026, pricing varies with the specific operational requirement and engagement duration."
---

{city}'s ground transport is where the security picture translates most directly into operational decisions. {c['threat_note']}. A vetted security driver with pre-surveyed routes, operations controller oversight, and pre-arranged airport collection addresses the specific vulnerabilities that standard taxi and ride-share services leave open.

## The transfer security picture in {city}

The {c['airport_name']} arrival and the first vehicle movement into the city centre carry a concentrated risk window: visible luggage, unfamiliar surroundings, and the transition from a secured terminal to open-road movement. Pre-arranged inside-terminal collection, a security-checked vehicle, and a pre-surveyed route remove the exposure that kerbside collection creates.

For principals moving between {c['area1']}, {c['area2']}, and {c['area3']}, consistent route variation, traffic-aware timing, and operations controller cover are the operational norms. The {c['crime_report']} informs route selection decisions for every principal movement.

## Licensing and verification

All security drivers engaged for commercial principal movement in {city} must hold a current licence under the {c['license_law']}. Verification via the {c['license_body']} public register is the standard check before engagement.

For complementary services in {city}, see our [{city} city security briefing](/cities/{slug}/) and our [bodyguard hire in {city}](/bodyguard-hire/{slug}/).
"""
    return content


def ep_page(c):
    slug = list(k for k, v in CITY_DATA.items() if v["city"] == c["city"])[0]
    city = c["city"]
    country = c["country"]
    title = f"Executive Protection in {city}, {country}"
    if len(title) > 70:
        title = f"Executive Protection in {city}"
    seo_title = f"Executive Protection {city} | {country} EP Services"
    if len(seo_title) > 70:
        seo_title = f"Executive Protection {city} | EP Services"
    desc = (f"Comprehensive executive protection in {city}, {country}. "
            f"Licensed close protection officers, secure transport, venue advance "
            f"work, and pre-travel threat assessment.")
    if len(desc) > 175:
        desc = desc[:172] + "..."
    desc = desc[:175]

    armed_str = ("All close protection in this jurisdiction is unarmed; "
                 "armed response is a police function." if c["unarmed"] else
                 f"{c['armed_detail'].capitalize()}.")

    content = f"""---
title: "{clean(title)}"
description: "{clean(desc)}"
slug: "{slug}"
h1: "Executive Protection Services in {city}, {country}"
seo_title: "{clean(seo_title)}"
service: "executive-protection"
city: "{city}"
country: "{country}"
risk_level: "{c['risk_level']}"
hero_image: "{c['hero_image']}"
date: "2026-06-18"
cta_text: "Planning a {city} visit? Request an EP brief before confirming your itinerary."
components:
  - title: "Pre-Travel Threat Assessment"
    description: "Written threat assessment covering the current {city} security environment per {c['crime_report']}, risks specific to the principal's sector and profile, and itinerary-specific risk points including the {c['airport_code']} transfer, accommodation zone in {c['area1']} or {c['area2']}, and key meeting venues."
  - title: "Licensed Close Protection Officers"
    description: "Close protection officers in {city} must hold a current licence under the {c['license_law']}, administered by the {c['license_body']}. Every CPO deployed is verified against the relevant public register before engagement. {armed_str}"
  - title: "Secure Vehicle and Vetted Driver"
    description: "Appropriate-spec vehicle with a vetted security driver licensed under the {c['license_short']}. Route planning addresses the specific conditions in {city}: the {c['airport_code']} corridor, the {c['area1']} and {c['area2']} business districts, and any movement to secondary venues."
  - title: "Venue Advance Work"
    description: "Pre-principal reconnaissance of each key meeting venue in {city}: access and exit points, emergency exit routes, ambient security standard, proximity to {c['hosp1_name']}, and the response time of local emergency services. Brief to the CP team before the principal arrives."
  - title: "Operations Controller"
    description: "Dedicated operations controller throughout the visit. Check-ins at each movement. Welfare protocols triggered on any overdue contact. Incident escalation contact maintained with the principal's home-country team throughout the {city} engagement."
  - title: "HNWI and Extended EP Options"
    description: "For HNWI clients relocating to or visiting {city} on longer stays, options include residential security assessment for {c['residential_area']} properties, domestic staff vetting, and ongoing EP retainer arrangements in addition to visit-based close protection."
faqs:
  - question: "What does executive protection in {city} typically involve?"
    answer: "A standard {city} EP engagement includes a pre-travel written threat assessment based on {c['crime_report']}, a licensed close protection officer for all principal movements, a vetted security driver, venue advance work at key locations in {c['area1']} and {c['area2']}, and operations controller oversight throughout. For principals with elevated profiles, a two-officer team may be appropriate."
  - question: "What licensing applies to executive protection in {country}?"
    answer: "Close protection in {city} is governed by the {c['license_law']}, administered by the {c['license_body']}. All operators must hold a current licence and pass background checks. {armed_str} Verify operator licence status via the {c['license_body']} public register before engagement."
  - question: "What is the difference between a security driver and executive protection in {city}?"
    answer: "A security driver provides vetted, pre-surveyed ground transport with operations controller cover. Executive protection adds a close protection officer who accompanies the principal, conducts venue advance work, manages access at meetings and events, and provides a protective presence beyond the vehicle environment. For senior executives in {city}, both are typically part of the same protective detail."
  - question: "What does executive protection cost in {city}?"
    answer: "A single-officer EP engagement in {city} typically ranges from {c['ep_cost']} inclusive of driver and vehicle. Two-officer teams and extended-duration visits are priced individually. As at June 2026, pricing depends on the threat profile, team configuration, itinerary complexity, and whether advance work is included."
---

Executive protection in {city} is defined by the specific conditions documented in {c['crime_report']}: {c['threat_note']}. A structured EP engagement, starting with a pre-travel threat assessment and covering CPO cover for all movements, venue advance work, and operations controller oversight, addresses the specific risk factors rather than a generic security package.

## The EP requirement in {city}

For visiting corporate executives, {city} EP typically begins with a licensed close protection officer for meetings, events, and movements where a protective presence is warranted, combined with a vetted security driver for all vehicle movements. The {c['license_law']} provides the licensing framework that governs all commercial close protection work in {c['country']}.

The threat picture in {c['area1']}, {c['area2']}, and {c['area3']} is {c['risk_level']} by international standards, with the specific conditions set out in {c['crime_report']} shaping operational planning. {c['advisory_fcdo'].capitalize() if not c['advisory_fcdo'][0].isupper() else c['advisory_fcdo']} is the relevant UK government advisory position.

## Licensing and compliance

Every CPO and operator engaged for {city} EP work must hold a current licence under the {c['license_short']}. The {c['license_body']} maintains a public register for licence verification, which is the standard client-side compliance check before engagement.

Emergency cover in {city}: {c['emergency']} (emergency services). Primary facilities: {c['hosp1_name']} ({c['hosp1_tel']}) and {c['hosp2_name']} ({c['hosp2_tel']}).

For related services in {city}, see our [{city} city security briefing](/cities/{slug}/), [security drivers in {city}](/security-drivers/{slug}/), and [bodyguard hire in {city}](/bodyguard-hire/{slug}/).
"""
    return content


def rs_page(c):
    slug = list(k for k, v in CITY_DATA.items() if v["city"] == c["city"])[0]
    city = c["city"]
    country = c["country"]
    title = f"Residential Security in {city}, {country}"
    if len(title) > 70:
        title = f"Residential Security in {city}"
    seo_title = f"Residential Security {city} | {country} Home Protection"
    if len(seo_title) > 70:
        seo_title = f"Residential Security {city} | Home Protection"
    desc = (f"Residential security for expatriates and executives in {city}, "
            f"{country}. Property assessment, vetted guarding, domestic staff "
            f"vetting, and safe-room planning.")
    if len(desc) > 175:
        desc = desc[:172] + "..."
    desc = desc[:175]

    armed_str = ("Close protection in this jurisdiction is unarmed." if c["unarmed"]
                 else f"{c['armed_detail'].capitalize()}.")

    content = f"""---
title: "{clean(title)}"
description: "{clean(desc)}"
slug: "{slug}"
h1: "Residential Security in {city}, {country}"
seo_title: "{clean(seo_title)}"
service: "residential-security"
city: "{city}"
country: "{country}"
risk_level: "{c['risk_level']}"
hero_image: "{c['hero_image']}"
date: "2026-06-18"
cta_text: "Moving to or staying in {city}? Request a residential security assessment."
components:
  - title: "Property Security Assessment"
    description: "Written assessment of the property in {city}: perimeter (walls, fencing, CCTV coverage and blind spots), access control (key and code management), alarm system standard, emergency response provision, and shelter-in-place capability. Assessment informed by the local risk picture per {c['crime_report']}."
  - title: "Vetted Manned Guarding"
    description: "Where the property and threat profile warrant it, manned guarding from operators licensed under the {c['license_law']}, administered by the {c['license_body']}. Guarding schedules are built around the specific risk picture for {c['residential_area']} properties."
  - title: "Alarm and Response Integration"
    description: "Assessment of the current alarm system and response provider, including response time in the specific {city} neighbourhood and capability on arrival. Where the existing provider is not appropriate, alternatives are identified as part of the assessment output."
  - title: "Domestic Staff Vetting"
    description: "Background checks on household staff with property access: criminal record check (via the appropriate authority in {country}), identity verification, reference checks with previous employers, and employment contract review for key control and access-hour clarity."
  - title: "Safe Room and Shelter-in-Place Planning"
    description: "Assessment of existing safe-room capability or identification of the most defensible space in the property. Communication equipment, shelter-in-place protocol, and the emergency contact chain, including {c['hosp1_name']} ({c['hosp1_tel']}) and emergency number {c['emergency']}."
  - title: "Ongoing Audit and Review"
    description: "For permanent or long-term {city} residents, a recurring security assessment identifies changes in the property's surroundings, local incident patterns per {c['crime_report']}, or property modifications that affect the security picture. Annual review is standard for senior expatriates."
faqs:
  - question: "What are the most common residential security gaps for executives in {city}?"
    answer: "The most consistently identified gaps in {city} residential security assessments are: CCTV systems with significant blind spots or inadequate night-vision capability; domestic staff without formal background checks who have unsupervised property access; alarm response providers with slow response times in the specific district; and no shelter-in-place or safe-room plan. These gaps apply across {c['residential_area']} properties regardless of the building's general standard."
  - question: "Do I need manned guarding for a residential property in {city}?"
    answer: "Manned guarding is warranted where the property assessment identifies specific risk factors: no alternative access control, isolated location, elevated neighbourhood risk per {c['crime_report']}, or a principal profile that increases targeting likelihood. For most corporate executive residences in {c['area1']} and {c['area2']}, an alarm system with a reliable response provider, staff vetting, and CCTV coverage is the appropriate starting baseline."
  - question: "How is domestic staff vetting conducted in {city}?"
    answer: "Domestic staff vetting in {city} covers: a criminal record check through the appropriate {country} authority, identity document verification, reference checks with previous employers in {country} (specifically confirming property access and conduct), and a review of the employment contract for clarity on access hours and key control. People with access to your property when you are away are the primary insider-threat variable in residential security."
  - question: "What does a residential security assessment cost in {city}?"
    answer: "A property security assessment in {city} typically ranges from {c['rs_cost']}. As at June 2026, cost varies with property size, complexity, and whether the assessment includes a written report with vendor recommendations or just the initial inspection."
---

Residential security in {city} is primarily about identifying the specific gaps in an existing security arrangement rather than starting from zero. {c['threat_note']}. For expatriate and executive residents in {c['residential_area']}, the assessment process identifies whether the current alarm, guarding, staff vetting, and CCTV arrangements are appropriate for the actual risk picture.

## The residential risk in {city}

{c['crime_report']} provides the baseline risk data for {city}. For residential security planning, the relevant variables are the incident pattern in the specific neighbourhood of the property, the response capability of any current alarm or guarding provider, and the access controls in place for household staff and service contractors.

## What a residential security assessment covers

A {city} residential security assessment covers: perimeter and access control, CCTV coverage and gaps, alarm and response provision (including tested response times), domestic staff vetting status, and shelter-in-place capability. The output is a written report with prioritised recommendations, not a sales exercise for unnecessary equipment.

For related services, see our [{city} city security briefing](/cities/{slug}/), [executive protection in {city}](/executive-protection/{slug}/), and [bodyguard hire in {city}](/bodyguard-hire/{slug}/).
"""
    return content


def es_page(c):
    slug = list(k for k, v in CITY_DATA.items() if v["city"] == c["city"])[0]
    city = c["city"]
    country = c["country"]
    title = f"Event Security in {city}, {country}"
    if len(title) > 70:
        title = f"Event Security in {city}"
    seo_title = f"Event Security {city} | {country} Corporate Events"
    if len(seo_title) > 70:
        seo_title = f"Event Security {city} | Corporate Events"
    desc = (f"Event security in {city} for corporate conferences, private functions, "
            f"and executive events. Venue assessment, close protection, and "
            f"access control from licensed operators.")
    if len(desc) > 175:
        desc = desc[:172] + "..."
    desc = desc[:175]

    armed_str = ("All event security in this jurisdiction is unarmed; armed "
                 "response is a police function." if c["unarmed"] else
                 f"{c['armed_detail'].capitalize()}.")

    content = f"""---
title: "{clean(title)}"
description: "{clean(desc)}"
slug: "{slug}"
h1: "Event Security in {city}, {country}"
seo_title: "{clean(seo_title)}"
service: "event-security"
city: "{city}"
country: "{country}"
risk_level: "{c['risk_level']}"
hero_image: "{c['hero_image']}"
date: "2026-06-18"
cta_text: "Planning an event in {city}? Security planning starts with the venue assessment."
components:
  - title: "Venue Security Assessment"
    description: "Assessment of the event venue in {city} covering: access and exit points, perimeter control, vehicle access management, CCTV coverage, emergency exit routes, proximity to {c['hosp1_name']} ({c['hosp1_tel']}), and ambient security standard. {c['event_venue']} venues have significantly different security profiles and are assessed individually."
  - title: "Close Protection for Principals and VIPs"
    description: "Licensed close protection officers for executives, keynote speakers, and high-profile guests at {city} events. All operators hold a current licence under the {c['license_law']}. {armed_str}"
  - title: "Access Control"
    description: "Managed entry with credential verification and, where appropriate, bag search. In {city}, access control is a functional security measure for corporate events, not a ceremonial one. Protocols are scaled to the event size, venue type, and the assessed risk profile."
  - title: "Event Transport Security"
    description: "Secure transfers for delegates, executives, and VIPs between accommodation, the venue, and {c['airport_code']}. Route planning accounts for the {city} traffic environment and the current incident pattern per {c['crime_report']}. Operations controller cover is maintained throughout all transfers."
  - title: "Crowd and Public-Space Awareness"
    description: "{city} events in {c['event_venue']} require crowd-space awareness appropriate to the specific venue type. Outdoor events, multi-venue programmes, and events near high-footfall public areas require additional advance planning. The {c['key_threat']} picture informs the specific protocols applied."
  - title: "Emergency Response Planning"
    description: "Written emergency protocols covering medical incidents, security threats, and evacuation. Includes liaison with {c['hosp1_name']} ({c['hosp1_tel']}) and {c['hosp2_name']} ({c['hosp2_tel']}). Emergency number in {city}: {c['emergency']}. Protocols are briefed to all team members before the event."
faqs:
  - question: "What does event security in {city} typically involve?"
    answer: "A {city} event security engagement typically covers: venue security assessment, access control with credential verification, licensed close protection officers for key principals, secure transport for delegates between accommodation and venue, and written emergency protocols. The scale of provision depends on the event size, venue type, and the risk profile of attendees per {c['crime_report']}."
  - question: "Which venues in {city} are suitable for corporate events?"
    answer: "{c['event_venue']} represent the primary corporate event locations in {city}, with established security infrastructure. Venue selection has security implications beyond hospitality quality: access control capability, perimeter management, vehicle access points, and proximity to emergency services are all relevant factors assessed before recommending a venue."
  - question: "What licensing standard applies to event security operators in {country}?"
    answer: "Event security operators in {city} must hold current licences under the {c['license_law']}, administered by the {c['license_body']}. {armed_str} Operators are vetted and carry appropriate insurance. Verify licence status via the {c['license_body']} public register before engagement."
  - question: "How is emergency planning handled for events in {city}?"
    answer: "Emergency planning for {city} events covers medical incident response, security threat protocols, and evacuation procedures. Key emergency contacts: {c['emergency']} (emergency services), {c['hosp1_name']} ({c['hosp1_tel']}), {c['hosp2_name']} ({c['hosp2_tel']}). Written protocols are prepared and briefed to all security team members before the event opens."
---

{city} is an established corporate event destination, and the security planning that underpins events in {c['event_venue']} should start with the specific conditions documented in {c['crime_report']}: {c['threat_note']}. Venue selection, access control, VIP close protection, and delegate transport are the four planning layers that define whether a {city} corporate event runs without incident.

## Event security planning for {city}

Venue selection is the first security decision: the access control capability, vehicle management, perimeter security, and proximity to emergency services vary significantly between {c['event_venue']} venues. A venue with a controlled vehicle access point, operating CCTV, and proximity to {c['hosp1_name']} starts from a better position than one without these features.

Transport is a consistent requirement for events in {city}. Delegate transfers between accommodation in {c['area1']} or {c['area2']} and the event venue should be pre-arranged with vetted, licensed drivers, not organised ad hoc on the day.

## Operator licensing

All event security operators in {city} must hold a current licence under the {c['license_short']}. The {c['license_body']} maintains the register. {armed_str}

For broader security services in {city}, see our [{city} city security briefing](/cities/{slug}/) and our [event security service overview](/services/event-security/).
"""
    return content


def cpo_page(c):
    slug = list(k for k, v in CITY_DATA.items() if v["city"] == c["city"])[0]
    city = c["city"]
    country = c["country"]
    title = f"Close Protection Officers in {city}, {country}"
    if len(title) > 70:
        title = f"Close Protection Officers in {city}"
    seo_title = f"Close Protection Officers {city} | Licensed CPOs"
    if len(seo_title) > 70:
        seo_title = f"Close Protection Officers {city}"
    desc = (f"Licensed close protection officers in {city}, {country}. "
            f"Vetted CPOs for corporate and HNWI principals across "
            f"{c['area1']}, {c['area2']}, and {c['area3']}.")
    if len(desc) > 175:
        desc = desc[:172] + "..."
    desc = desc[:175]

    armed_str = ("Close protection in this jurisdiction is unarmed; armed "
                 "response is a police function." if c["unarmed"] else
                 f"{c['armed_detail'].capitalize()}.")

    content = f"""---
title: "{clean(title)}"
description: "{clean(desc)}"
slug: "{slug}"
h1: "Close Protection Officers in {city}, {country}"
seo_title: "{clean(seo_title)}"
service: "close-protection-officers"
city: "{city}"
country: "{country}"
risk_level: "{c['risk_level']}"
hero_image: "{c['hero_image']}"
date: "2026-06-18"
cta_text: "Planning a {city} detail? Speak to us about licensed CPO cover before confirming accommodation and transport."
components:
  - title: "Licensing Standard for {city} CPOs"
    description: "Close protection officers operating commercially in {city} must hold a current licence under the {c['license_law']}, administered by the {c['license_body']}. Licence verification via the relevant public register is the standard check before any CPO is deployed on a {city} engagement."
  - title: "Threat-Specific Operational Planning"
    description: "Operational planning for {city} CPO deployments addresses the specific conditions set out in {c['crime_report']}: {c['threat_note']}. Planning covers route selection, departure timing, venue pre-advance, and contingency protocols for the {c['area1']} and {c['area2']} operating areas."
  - title: "Armed and Unarmed Cover Options"
    description: "{armed_str} For most corporate principals in {city}, unarmed CPO cover with threat-aware route planning and operations controller oversight meets the risk picture. The decision on armed cover, where applicable, is made against the specific threat assessment."
  - title: "Venue Advance Work"
    description: "Pre-principal advance of each key venue in {city}: access points, emergency exits, ambient security standard, proximity to {c['hosp1_name']} ({c['hosp1_tel']}), and evacuation routes. The advance brief is provided to the CPO team before the principal's arrival at each location."
  - title: "Operations Controller"
    description: "Every {city} CPO detail is backed by an operations controller tracking location, maintaining the operational timeline, and holding the emergency contact chain including {c['emergency']} (emergency services) and {c['hosp1_name']} ({c['hosp1_tel']}). The controller converts individual CPO cover into a coherent protective operation."
  - title: "Transport Integration"
    description: "CPO cover in {city} frequently incorporates a vetted security driver as a second team member. Drivers hold a current licence under the {c['license_short']} and are trained for the {city} operating environment. The CPO-plus-driver configuration is the standard team for principal movements in {c['area1']} and {c['area2']}."
faqs:
  - question: "What licence does a close protection officer need in {city}?"
    answer: "A close protection officer providing commercial close protection in {city} must hold a current licence under the {c['license_law']}, administered by the {c['license_body']}. Ask for the specific licence number of any CPO proposed for your detail and verify it via the {c['license_body']} public register. {armed_str}"
  - question: "How is a close protection officer different from a bodyguard in {country}?"
    answer: "Close protection officer is the professional and regulatory term for commercially licensed personal security work in {country}. Bodyguard is not a separate licence category. The distinction that matters operationally is between licensed CPOs who have completed an approved CP qualification and hold a valid licence, and unlicensed individuals. Always verify the licence before engagement."
  - question: "How is the decision between armed and unarmed CPO cover made in {city}?"
    answer: "{armed_str} Where armed cover is legally available, it is specified where the threat assessment identifies a specific elevated risk to the principal: a documented threat, sector exposure with a higher targeting history, or movement in areas where the {c['crime_report']} records elevated violent crime. The threat assessment, not a default preference, drives the decision."
  - question: "What does a close protection officer cost per day in {city}?"
    answer: "A single licensed CPO in {city} typically ranges from {c['cpo_cost']} depending on experience, licensing level, and the specific operational requirement. Transport integration, advance work, and operations controller time are costed separately. As at June 2026, multi-day engagements and retainer arrangements are priced individually."
---

{city}'s close protection officer market is defined by the {c['license_law']}, which sets the licensing standard for all commercial CPO work in {country}. {c['threat_note']}. For corporate principals with visits to {c['area1']}, {c['area2']}, and {c['area3']}, a licensed CPO with operations controller support and pre-advance venue work is the appropriate operational baseline given the {c['risk_level']} risk environment.

## The licensing framework in {city}

The {c['license_body']} administers the licensing of close protection officers in {city} under the {c['license_short']}. Licence verification is the primary compliance step for any client engaging CPO services: ask for the licence number and confirm it via the public register before deployment begins.

{armed_str}

## What CPO cover looks like in {city}

A {city} CPO engagement typically involves venue advance work at the principal's accommodation, meeting locations in {c['area1']} and {c['area2']}, and any event venues; operations controller oversight throughout; and coordinated vehicle movements with a licensed security driver. The operational protocols are informed by the specific conditions in {c['crime_report']}.

For complementary services in {city}, see our [{city} city security briefing](/cities/{slug}/) and [bodyguard hire in {city}](/bodyguard-hire/{slug}/).
"""
    return content


SERVICES = [
    ("security-drivers", sd_page),
    ("executive-protection", ep_page),
    ("residential-security", rs_page),
    ("event-security", es_page),
    ("close-protection-officers", cpo_page),
]

CITIES = [
    "atlanta", "boston", "chicago", "houston", "los-angeles",
    "manchester", "osaka", "san-francisco", "taipei", "vancouver",
]

created = 0
skipped = 0
for service, page_fn in SERVICES:
    svc_dir = os.path.join(CONTENT_ROOT, service)
    for city_slug in CITIES:
        c = CITY_DATA[city_slug]
        out_path = os.path.join(svc_dir, f"{city_slug}.md")
        if os.path.exists(out_path):
            print(f"SKIP (exists): {service}/{city_slug}.md")
            skipped += 1
            continue
        content = page_fn(c)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"CREATED: {service}/{city_slug}.md")
        created += 1

print(f"\nDone. Created: {created}, Skipped: {skipped}, Total: {created + skipped}")
