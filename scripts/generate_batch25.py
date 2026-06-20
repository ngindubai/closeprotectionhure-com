#!/usr/bin/env python3
"""
generate_batch25.py
Generates 50 Hugo content pages: 5 services x 10 cities for CloseProtectionHire.com
Run from any directory. Creates files in site/content/<service>/<city>.md

Services: security-drivers, executive-protection, residential-security,
          event-security, close-protection-officers
Cities: atlanta, boston, chicago, houston, los-angeles, manchester, osaka,
        san-francisco, taipei, vancouver
"""

import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Resolve base path relative to this script
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
CONTENT_DIR = BASE_DIR / "site" / "content"

# ---------------------------------------------------------------------------
# City data
# ---------------------------------------------------------------------------
CITIES = {
    "atlanta": {
        "name": "Atlanta",
        "country": "United States",
        "risk_level": "moderate",
        "licensing": "Private Detective and Security Agencies Act (OCGA Title 43, Ch 38), Georgia Secretary of State",
        "licensing_short": "OCGA Title 43, Ch 38",
        "license_body": "Georgia Secretary of State",
        "airport": "Hartsfield-Jackson ATL, ~17km south, 25-40 min",
        "airport_code": "ATL",
        "airport_short": "Hartsfield-Jackson ATL",
        "areas": "Buckhead, Midtown, Sandy Springs",
        "emergency": "911",
        "hospitals": "Emory University Hospital 404-712-2000; Grady Memorial 404-616-1000",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "carjacking citywide (APD Crime Report 2025)",
        "crime_source": "APD Crime Report 2025",
        "armed": "Georgia Weapons Carry Licence",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$350 to $650",
        "ep_day_rate": "$600 to $1,100",
        "rs_month_rate": "$3,500 to $7,000 per month",
        "cpo_day_rate": "$500 to $900",
        "es_day_rate": "$400 to $750",
        "district_note": "Buckhead business corridor and Midtown high-rises",
        "transport_note": "I-285 perimeter and I-75/I-85 downtown connector",
        "industry_note": "CNN, Delta Air Lines, Coca-Cola, and a concentration of Fortune 500 regional headquarters",
        "event_note": "State Farm Arena, Mercedes-Benz Stadium, and the Georgia World Congress Center",
        "res_note": "Buckhead residential enclave and Sandy Springs gated communities",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "Licensed operators may carry under a Georgia Weapons Carry Licence where the engagement requires it.",
        "unarmed_note": "Most corporate CP engagements in Atlanta use unarmed personnel, with armed options available based on assessed threat.",
    },
    "boston": {
        "name": "Boston",
        "country": "United States",
        "risk_level": "low",
        "licensing": "Massachusetts Private Detective and Watch, Guard or Patrol Agency Licensing Act (MGL c.147, ss.22-30), Massachusetts Department of Public Safety",
        "licensing_short": "MGL c.147, ss.22-30",
        "license_body": "Massachusetts Department of Public Safety",
        "airport": "Logan International BOS, ~5km from Downtown, 15-30 min",
        "airport_code": "BOS",
        "airport_short": "Logan International BOS",
        "areas": "Financial District, Back Bay, Seaport, Cambridge",
        "emergency": "911",
        "hospitals": "Brigham and Women's 617-732-5500; Massachusetts General 617-726-2000",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "very low; event-security context (2013 Marathon bombing per BPD 2025); localised crime Roxbury",
        "crime_source": "BPD Crime Report 2025",
        "armed": "Massachusetts restrictive firearms licensing (MGL)",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$300 to $550",
        "ep_day_rate": "$550 to $1,000",
        "rs_month_rate": "$3,000 to $6,500 per month",
        "cpo_day_rate": "$450 to $850",
        "es_day_rate": "$350 to $650",
        "district_note": "Financial District, Back Bay, and Seaport innovation hub",
        "transport_note": "Route 93 and the Ted Williams Tunnel from Logan",
        "industry_note": "biotech, higher education, and financial services sectors",
        "event_note": "TD Garden, Boston Convention and Exhibition Center, and Harvard-adjacent venues",
        "res_note": "Back Bay brownstones and Cambridge residential estates",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "Massachusetts imposes restrictive firearms licensing requirements; armed engagements require specialist legal review under MGL.",
        "unarmed_note": "Unarmed close protection is standard for corporate engagements in Boston given the city's low ambient threat level.",
    },
    "chicago": {
        "name": "Chicago",
        "country": "United States",
        "risk_level": "moderate",
        "licensing": "Illinois Private Detective, Private Alarm, Private Security, Fingerprint Vendor, and Locksmith Act 2004 (IDFPR)",
        "licensing_short": "Illinois PSISA 2004 (IDFPR)",
        "license_body": "Illinois Department of Financial and Professional Regulation",
        "airport": "O'Hare ORD ~27km, 35-50 min; Midway MDW ~16km, 25-40 min",
        "airport_code": "ORD",
        "airport_short": "O'Hare ORD",
        "areas": "The Loop, River North, Gold Coast, Magnificent Mile",
        "emergency": "911",
        "hospitals": "Northwestern Memorial 312-926-2000; Rush University Medical Center 312-942-5000",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "carjacking elevated citywide (CPD Crime Report 2025); neighbourhood crime disparity South/West Side",
        "crime_source": "CPD Crime Report 2025",
        "armed": "FOID card plus Illinois armed contractor endorsement",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$350 to $650",
        "ep_day_rate": "$600 to $1,100",
        "rs_month_rate": "$3,500 to $7,500 per month",
        "cpo_day_rate": "$500 to $950",
        "es_day_rate": "$400 to $800",
        "district_note": "The Loop financial core, River North hospitality district, and Gold Coast residential",
        "transport_note": "I-90/94 Dan Ryan and Kennedy expressways, with the Magnificent Mile on Michigan Avenue",
        "industry_note": "financial trading, commodities, law, and a large corporate events ecosystem",
        "event_note": "McCormick Place Convention Center, United Center, and Soldier Field",
        "res_note": "Gold Coast and Lincoln Park HNWI residential zones",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "Illinois armed contractor endorsement under IDFPR, plus a valid FOID card, is required for armed engagements in Chicago.",
        "unarmed_note": "Unarmed CP is standard for Loop and Magnificent Mile corporate work; armed options are available for elevated-risk engagements.",
    },
    "houston": {
        "name": "Houston",
        "country": "United States",
        "risk_level": "moderate",
        "licensing": "Texas Private Security Act (Texas Occupations Code Ch 1702), Texas DPS",
        "licensing_short": "Texas Occupations Code Ch 1702, Texas DPS",
        "license_body": "Texas Department of Public Safety",
        "airport": "Bush Intercontinental IAH ~37km north, 40-55 min; Hobby HOU ~19km south",
        "airport_code": "IAH",
        "airport_short": "Bush Intercontinental IAH",
        "areas": "Galleria/Uptown, River Oaks, Energy Corridor, Texas Medical Center",
        "emergency": "911",
        "hospitals": "Houston Methodist 713-790-3311; Memorial Hermann TMC 713-704-4000",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "property crime and vehicle theft elevated (HPD Crime Report 2025); energy-sector executive profiles",
        "crime_source": "HPD Crime Report 2025",
        "armed": "Texas armed security officer endorsement under TOC Ch 1702",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$300 to $600",
        "ep_day_rate": "$550 to $1,050",
        "rs_month_rate": "$3,200 to $6,800 per month",
        "cpo_day_rate": "$480 to $900",
        "es_day_rate": "$380 to $720",
        "district_note": "Galleria/Uptown commercial corridor and River Oaks residential district",
        "transport_note": "I-610 loop, I-10 Katy Freeway, and the Hardy Toll Road IAH approach",
        "industry_note": "energy, petrochemicals, healthcare, and international oilfield services executives",
        "event_note": "George R. Brown Convention Center, Minute Maid Park, and Toyota Center",
        "res_note": "River Oaks estates and the Memorial Villages gated communities",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "Texas armed security officer endorsement under TOC Ch 1702 is required for licensed armed protection in Houston.",
        "unarmed_note": "Unarmed close protection covers most corporate Galleria/Uptown and Energy Corridor engagements; armed options are assessed case by case.",
    },
    "los-angeles": {
        "name": "Los Angeles",
        "country": "United States",
        "risk_level": "moderate",
        "licensing": "California Bureau of Security and Investigative Services (BSIS), Business and Professions Code",
        "licensing_short": "California BSIS, Business and Professions Code",
        "license_body": "California BSIS",
        "airport": "LAX ~27km from Beverly Hills, 30-60 min variable",
        "airport_code": "LAX",
        "airport_short": "LAX",
        "areas": "Beverly Hills, Century City, Bel Air, Downtown Financial District",
        "emergency": "911",
        "hospitals": "Cedars-Sinai 310-423-3277; UCLA Medical Center 310-825-9111",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "vehicle crime and smash-and-grab (LAPD Crime Report 2025); neighbourhood disparity Skid Row/Hollywood Blvd",
        "crime_source": "LAPD Crime Report 2025",
        "armed": "California BSIS firearms permit plus Guard Card",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$400 to $750",
        "ep_day_rate": "$700 to $1,300",
        "rs_month_rate": "$4,000 to $8,500 per month",
        "cpo_day_rate": "$600 to $1,100",
        "es_day_rate": "$500 to $950",
        "district_note": "Beverly Hills commercial district, Century City corporate towers, and Bel Air residential",
        "transport_note": "the I-405 San Diego Freeway, the I-10 Santa Monica Freeway, and Sepulveda Boulevard as the primary LAX surface route",
        "industry_note": "entertainment, technology, and HNWI residential markets",
        "event_note": "Staples Center/Crypto.com Arena, the LA Convention Center, and private studio event spaces",
        "res_note": "Bel Air and Holmby Hills estates, and Beverly Hills gated residential",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "California BSIS firearms permit, in addition to the standard Guard Card, is required for any licensed armed engagement in Los Angeles.",
        "unarmed_note": "Unarmed CP is standard for most Beverly Hills and Century City corporate engagements; armed detail is available for elevated-risk principals.",
    },
    "manchester": {
        "name": "Manchester",
        "country": "United Kingdom",
        "risk_level": "low",
        "licensing": "Private Security Industry Act 2001, Security Industry Authority (SIA)",
        "licensing_short": "Private Security Industry Act 2001, SIA",
        "license_body": "Security Industry Authority (SIA)",
        "airport": "Manchester Airport MAN, ~14km south, 30-40 min via M56",
        "airport_code": "MAN",
        "airport_short": "Manchester Airport MAN",
        "areas": "Spinningfields, Deansgate, Salford Quays, Manchester Arena",
        "emergency": "999 (101 non-emergency)",
        "hospitals": "Manchester Royal Infirmary 0161-276-1234; Salford Royal 0161-206-1234",
        "advisory": "FCDO normal precautions for UK 2026; UK terrorism threat SUBSTANTIAL (MI5 2026)",
        "key_threat": "GMP Crime Report 2025: low corporate-area crime; elevated disorder Northern Quarter late-night; terrorism threat SUBSTANTIAL",
        "crime_source": "GMP Crime Report 2025",
        "armed": "UK close protection is unarmed (SIA law)",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "GBP",
        "currency_symbol": "GBP",
        "sd_day_rate": "GBP 350 to GBP 600",
        "ep_day_rate": "GBP 500 to GBP 950",
        "rs_month_rate": "GBP 2,800 to GBP 6,000 per month",
        "cpo_day_rate": "GBP 450 to GBP 850",
        "es_day_rate": "GBP 350 to GBP 700",
        "district_note": "Spinningfields legal and financial district, Deansgate hospitality corridor, and Salford Quays media campus",
        "transport_note": "the M60 orbital, the M56 Manchester Airport spur, and the Metrolink tram network",
        "industry_note": "media (ITV, BBC Manchester, MediaCityUK), legal and financial services, and a major events economy",
        "event_note": "Manchester Arena, Manchester Central Convention Complex, and Old Trafford for large-scale corporate and entertainment events",
        "res_note": "Altrincham, Hale, and the Cheshire commuter belt for HNWI residential cover",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "UK close protection is legally unarmed under the Private Security Industry Act 2001; SIA-licensed CPOs do not carry firearms.",
        "unarmed_note": "All SIA-licensed close protection in the UK, including Manchester, is conducted on an unarmed basis.",
    },
    "osaka": {
        "name": "Osaka",
        "country": "Japan",
        "risk_level": "low",
        "licensing": "Security Business Act (Act No.117 of 1972), Osaka Prefectural Police approval",
        "licensing_short": "Security Business Act No.117 of 1972, Osaka Prefectural Police",
        "license_body": "Osaka Prefectural Police",
        "airport": "Kansai International KIX ~50km, 75-90 min; Itami ITM ~15km, 30-40 min",
        "airport_code": "KIX",
        "airport_short": "Kansai International KIX",
        "areas": "Umeda/Kita CBD, Nakanoshima, Fukushima, Yodoyabashi",
        "emergency": "110 police; 119 ambulance",
        "hospitals": "Osaka University Hospital 06-6879-5111",
        "advisory": "FCDO normal precautions Japan 2026 with earthquake awareness; US State Dept Level 1",
        "key_threat": "very low crime (NPA Crime Statistics 2024/2025); petty theft Dotonbori crowds; seismic/natural disaster preparedness",
        "crime_source": "NPA Crime Statistics 2024/2025",
        "armed": "private armed CP not permitted in Japan",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "JPY",
        "currency_symbol": "JPY",
        "sd_day_rate": "JPY 50,000 to JPY 100,000",
        "ep_day_rate": "JPY 80,000 to JPY 160,000",
        "rs_month_rate": "JPY 400,000 to JPY 900,000 per month",
        "cpo_day_rate": "JPY 70,000 to JPY 140,000",
        "es_day_rate": "JPY 55,000 to JPY 110,000",
        "district_note": "Umeda/Kita CBD, Nakanoshima international hotel corridor, and Namba commercial district",
        "transport_note": "the Hanshin Expressway, the Kintetsu Osaka Line, and the Nankai Airport Express from KIX",
        "industry_note": "Panasonic, Sharp, Suntory, and a concentration of manufacturing and trading company headquarters",
        "event_note": "Intex Osaka convention centre, Maishima complex, and Osaka Prefectural Gymnasium for large-scale corporate gatherings",
        "res_note": "Senri Hills, Toyonaka, and North Osaka residential districts for HNWI cover",
        "cross_border": "",
        "visa": "Visa requirements vary by nationality; confirm entry conditions with the Japanese Embassy before travel.",
        "language": "Japanese is the working language; interpret and bilingual advance work support should be arranged for visiting international principals.",
        "armed_note": "Private armed close protection is not permitted under Japanese law; all engagements are conducted on an unarmed basis.",
        "unarmed_note": "All close protection in Japan is unarmed; operational effectiveness relies on advance planning and structured movement protocols.",
    },
    "san-francisco": {
        "name": "San Francisco",
        "country": "United States",
        "risk_level": "moderate",
        "licensing": "California Bureau of Security and Investigative Services (BSIS), Business and Professions Code",
        "licensing_short": "California BSIS, Business and Professions Code",
        "license_body": "California BSIS",
        "airport": "SFO ~21km south, 30-45 min",
        "airport_code": "SFO",
        "airport_short": "SFO",
        "areas": "Financial District, Pacific Heights, Marina District, Mission Bay",
        "emergency": "911",
        "hospitals": "Zuckerberg SF General 415-206-8000; UCSF Medical Center 415-476-1000",
        "advisory": "FCDO normal precautions 2026; US State Dept Level 1",
        "key_threat": "vehicle break-ins among highest in California (SFPD Crime Report 2025); Tenderloin/Civic Center disorder",
        "crime_source": "SFPD Crime Report 2025",
        "armed": "California BSIS firearms permit plus Guard Card",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "USD",
        "currency_symbol": "$",
        "sd_day_rate": "$400 to $780",
        "ep_day_rate": "$700 to $1,350",
        "rs_month_rate": "$4,200 to $9,000 per month",
        "cpo_day_rate": "$600 to $1,150",
        "es_day_rate": "$500 to $980",
        "district_note": "Financial District on California Street, Pacific Heights residential, and Mission Bay technology campus",
        "transport_note": "US-101 and I-280, with the Bay Bridge and Golden Gate approach corridors",
        "industry_note": "technology, venture capital, biotech, and a highly visible HNWI population",
        "event_note": "Moscone Convention Center, Chase Center, and the Ferry Building for corporate functions",
        "res_note": "Pacific Heights, Presidio Heights, and Sea Cliff residential enclaves",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "California BSIS firearms permit, alongside the standard Guard Card, is required for any licensed armed engagement in San Francisco.",
        "unarmed_note": "Unarmed CP is standard for technology-sector corporate engagements; armed options are assessed based on specific principal threat profiles.",
    },
    "taipei": {
        "name": "Taipei",
        "country": "Taiwan",
        "risk_level": "low",
        "licensing": "Private Security Services Industry Act 2009, National Police Agency (NPA), Ministry of the Interior (MOI)",
        "licensing_short": "Private Security Services Industry Act 2009, NPA/MOI",
        "license_body": "National Police Agency (NPA), Ministry of the Interior",
        "airport": "Taoyuan International TPE ~40km, 40-60 min; Songshan TSA ~5km",
        "airport_code": "TPE",
        "airport_short": "Taoyuan International TPE",
        "areas": "Xinyi District, Da'an District, Zhongzheng, Zhongshan",
        "emergency": "110 police; 119 ambulance",
        "hospitals": "National Taiwan University Hospital 02-2312-3456; Taipei Veterans General 02-2871-2121",
        "advisory": "FCDO normal precautions Taiwan 2026 with cross-strait note; US State Dept Level 1",
        "key_threat": "very low crime (Taiwan NPA Crime Statistics 2024); cross-strait strategic context for contingency planning only",
        "crime_source": "Taiwan NPA Crime Statistics 2024",
        "armed": "private armed CP not permitted in Taiwan",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "TWD",
        "currency_symbol": "TWD",
        "sd_day_rate": "TWD 8,000 to TWD 18,000",
        "ep_day_rate": "TWD 15,000 to TWD 32,000",
        "rs_month_rate": "TWD 80,000 to TWD 180,000 per month",
        "cpo_day_rate": "TWD 12,000 to TWD 26,000",
        "es_day_rate": "TWD 9,000 to TWD 20,000",
        "district_note": "Xinyi District corporate and luxury retail hub, Da'an residential, and Zhongzheng government district",
        "transport_note": "the National Freeway No.1 and No.2 corridors and the Taoyuan MRT Airport Line",
        "industry_note": "semiconductor manufacturing, technology, financial services, and government-adjacent organisations operating in the Taiwan market",
        "event_note": "Taipei International Convention Center (TICC), Taipei Arena, and the Nangang Exhibition Center",
        "res_note": "Da'an District, Tianmu, and Yangmingshan residential areas for HNWI and diplomatic community cover",
        "cross_border": "",
        "visa": "Entry requirements for Taiwan vary by nationality; confirm with the Taipei Economic and Cultural Office before travel.",
        "language": "Mandarin Chinese is the primary language; bilingual advance support is recommended for visiting international principals.",
        "armed_note": "Private armed close protection is not permitted under Taiwan law; all CP engagements are conducted on an unarmed basis.",
        "unarmed_note": "All close protection in Taiwan is unarmed under the Private Security Services Industry Act 2009.",
    },
    "vancouver": {
        "name": "Vancouver",
        "country": "Canada",
        "risk_level": "low",
        "licensing": "BC Security Services Act 2007, BC Ministry of Public Safety, Security Programs Division",
        "licensing_short": "BC Security Services Act 2007",
        "license_body": "BC Ministry of Public Safety, Security Programs Division",
        "airport": "YVR Vancouver International ~12km south, 25-35 min via Highway 99",
        "airport_code": "YVR",
        "airport_short": "YVR Vancouver International",
        "areas": "Coal Harbour, Yaletown, West End, Robson Street",
        "emergency": "911",
        "hospitals": "Vancouver General 604-875-4111; St. Paul's 604-682-2344",
        "advisory": "FCDO normal precautions Canada 2026; US State Dept Level 1",
        "key_threat": "Downtown Eastside opioid crisis elevated property crime (VPD Statistical Report 2025); vehicle break-ins central area; low violent crime overall",
        "crime_source": "VPD Statistical Report 2025",
        "armed": "private armed CP not permitted without specific federal authorisation in Canada",
        "hero_image": "Close-Protection-2560.webp",
        "currency": "CAD",
        "currency_symbol": "CAD",
        "sd_day_rate": "CAD 450 to CAD 850",
        "ep_day_rate": "CAD 700 to CAD 1,300",
        "rs_month_rate": "CAD 3,800 to CAD 8,500 per month",
        "cpo_day_rate": "CAD 600 to CAD 1,100",
        "es_day_rate": "CAD 480 to CAD 900",
        "district_note": "Coal Harbour waterfront corporate district, Yaletown technology and creative hub, and West End residential",
        "transport_note": "Highway 99 from YVR, the Trans-Canada Highway approach, and the Sea-to-Sky corridor for Whistler transfers",
        "industry_note": "mining, technology, film production, and Pacific Rim trade",
        "event_note": "Vancouver Convention Centre, Rogers Arena, and BC Place for large-scale corporate and entertainment events",
        "res_note": "Shaughnessy, Kerrisdale, and West Point Grey for HNWI residential cover",
        "cross_border": "",
        "visa": "",
        "language": "",
        "armed_note": "Private armed close protection in Canada requires specific federal authorisation; the overwhelming majority of engagements in Vancouver are conducted on an unarmed basis.",
        "unarmed_note": "Unarmed close protection is the standard and legal baseline for private security in British Columbia.",
    },
}

CITY_ORDER = [
    "atlanta", "boston", "chicago", "houston", "los-angeles",
    "manchester", "osaka", "san-francisco", "taipei", "vancouver",
]

# ---------------------------------------------------------------------------
# Service definitions
# ---------------------------------------------------------------------------
SERVICES = ["security-drivers", "executive-protection", "residential-security",
            "event-security", "close-protection-officers"]

# ---------------------------------------------------------------------------
# Content generators — one per service
# ---------------------------------------------------------------------------

def gen_security_drivers(city_slug, c):
    name = c["name"]
    country = c["country"]
    seo_title = f"Security Driver {name} | {country} Vetted Transfers"
    if len(seo_title) > 70:
        seo_title = f"Security Driver {name} | Vetted {country} Transfer"
    if len(seo_title) > 70:
        seo_title = f"Security Driver {name} | Vetted Transfers"

    title = f"Security Drivers in {name}"
    h1 = f"Security Drivers in {name}, {country}"
    desc_raw = (
        f"Vetted, licensed security drivers in {name}. Airport transfers, "
        f"corporate routes, and HNWI movements across {c['areas']}."
    )
    # trim description to 120-175 chars
    description = desc_raw[:175]

    cta_text = (
        f"Travelling to {name} for a corporate programme or sensitive engagement? "
        f"Request a vetted security driver."
    )

    components = [
        {
            "title": f"Driver Licensing Under {c['licensing_short']}",
            "description": (
                f"Security drivers operating in {name} must hold a valid commercial driving licence "
                f"and work for a company licensed under {c['licensing']}. "
                f"Principals should request written confirmation of both the individual driver's credentials "
                f"and the operating company's registration before engagement. "
                f"This dual-compliance framework distinguishes a vetted security driver from a standard hire vehicle."
            ),
        },
        {
            "title": f"{c['airport_short']}: Collection and Route Planning",
            "description": (
                f"{c['airport']}. Security drivers conduct meet-and-greet at the designated arrivals "
                f"collection point; inside-terminal collection with a name board is standard for HNWI and senior "
                f"executive arrivals. Departure timing accounts for {name}'s typical traffic patterns on "
                f"{c['transport_note']}, with at least one alternative route planned to avoid predictable exposure."
            ),
        },
        {
            "title": "Counter-Surveillance and Route Variation",
            "description": (
                f"The primary security driver discipline in {name} is route variation across "
                f"{c['transport_note']}. Fixed routes at fixed times create a pattern that can be exploited; "
                f"security drivers rotate approaches to {c['areas']} based on time of day, traffic conditions, "
                f"and the specific threat level identified in the pre-travel assessment. "
                f"The key threat context noted in the {c['crime_source']} is: {c['key_threat']}."
            ),
        },
        {
            "title": "Driver Vetting and Background Screening",
            "description": (
                f"All security drivers deployed in {name} are subject to enhanced background screening "
                f"appropriate to the licensed operating environment: criminal records check, driving licence "
                f"endorsement history, and reference verification. The vetting standard is documented and "
                f"available on request. Screening is renewed on a periodic cycle; principals undertaking "
                f"recurring visits to {name} may request a named driver retained across engagements."
            ),
        },
        {
            "title": "Operations Controller Integration",
            "description": (
                f"Every security driver engagement in {name} is supported by a dedicated operations controller "
                f"monitoring the vehicle's position and maintaining communication throughout each journey. "
                f"The controller receives real-time updates at pre-agreed waypoints and holds a contingency "
                f"protocol for route deviation, vehicle breakdown, and medical emergency. "
                f"Emergency services in {name}: {c['emergency']}; hospitals: {c['hospitals']}."
            ),
        },
        {
            "title": "Vehicle Selection and Night/Peak-Hour Protocols",
            "description": (
                f"Vehicle selection for {name} security driver operations balances comfort, discretion, "
                f"and suitability for the road environment. Executive saloons and mid-size SUVs are the "
                f"standard platform; low-profile colour and specification choices reduce the visual signature "
                f"appropriate to {c['district_note']}. Night and peak-hour protocols increase following distances, "
                f"add journey-time buffers, and ensure vehicle fuelling is maintained above the half-tank threshold."
            ),
        },
    ]

    faqs = [
        {
            "question": f"Why choose a security driver over a standard taxi or ride-share in {name}?",
            "answer": (
                f"Standard taxis and ride-share drivers in {name} are not vetted to a security standard, "
                f"do not receive counter-surveillance training, and are not integrated into an operations "
                f"controller network. A security driver provides a documented chain of vetting, route variation "
                f"discipline, and real-time controller monitoring that ride-share platforms cannot replicate. "
                f"The {c['crime_source']} identifies: {c['key_threat']}, which makes unvetted vehicle use a "
                f"material exposure point for HNWI and senior executive principals."
            ),
        },
        {
            "question": f"What licence must a security driver hold to operate in {name}?",
            "answer": (
                f"Security drivers in {name} operate under {c['licensing']}. "
                f"The employing company must hold a valid licence or registration from the {c['license_body']}, "
                f"and individual drivers must hold the relevant commercial driving credentials. "
                f"Principals should request written confirmation of both before any engagement commences."
            ),
        },
        {
            "question": f"How does {c['airport_short']} collection work in practice?",
            "answer": (
                f"{c['airport_short']} ({c['airport_code']}) serves as the primary arrival point for most "
                f"visiting principals. The security driver pre-positions in the vehicle collection area; "
                f"for HNWI and senior executive arrivals, inside-terminal meet-and-greet with a name board "
                f"is arranged. Flight monitoring accounts for delays; the driver departs the collection area "
                f"only on confirmation of baggage clearance. Transfer time: {c['airport']}."
            ),
        },
        {
            "question": f"What does a security driver cost per day in {name}, as at June 2026?",
            "answer": (
                f"Security driver day rates in {name} range from approximately {c['sd_day_rate']} per day, "
                f"as at June 2026, depending on vehicle specification, engagement duration, and whether "
                f"full operations controller integration is included. Single-transfer pricing is available "
                f"for one-off airport or venue movements; multi-day corporate programme rates apply a "
                f"reduced daily rate for commitments of three or more consecutive days."
            ),
        },
    ]

    body = f"""\
{name} presents a security driver environment shaped by {c['key_threat'].split(';')[0]}. \
For HNWI principals and corporate executives visiting {c['district_note']}, \
vetted security drivers licensed under {c['licensing_short']} provide a materially \
different standard of vehicle cover from the standard hire vehicle market. \
The {c['crime_source']} informs the route planning and counter-surveillance protocols \
applied on {name}'s principal movement corridors.

## Licensing and compliance in {name}

Security driver companies operating in {name} are licensed under {c['licensing']}. \
Confirming the operating company's licence status and the individual driver's credentials \
with the {c['license_body']} is the standard due-diligence step before any \
engagement. {c['armed_note']}

## {c['airport_short']} and city movement

{c['airport_short']} ({c['airport_code']}) is the main gateway for visiting principals, with transfer times \
of {c['airport']}. Security drivers apply route variation on {c['transport_note']} \
and pre-plan alternative approaches to venues in {c['areas']} to reduce the predictability \
that fixed routing creates.

For complementary security services in {name}, see our [{name} city page](/cities/{city_slug}/) \
and [bodyguard hire in {name}](/bodyguard-hire/{city_slug}/).\
"""

    return _render_page(
        title=title, description=description, slug=city_slug, h1=h1,
        seo_title=seo_title, service="security-drivers", city=name,
        country=country, risk_level=c["risk_level"], hero_image=c["hero_image"],
        cta_text=cta_text, components=components, faqs=faqs, body=body,
    )


def gen_executive_protection(city_slug, c):
    name = c["name"]
    country = c["country"]
    seo_title = f"Executive Protection {name} | {country} EP Services"
    if len(seo_title) > 70:
        seo_title = f"Executive Protection {name} | EP Services"

    title = f"Executive Protection in {name}"
    h1 = f"Executive Protection Services in {name}, {country}"
    description = (
        f"Licensed executive protection in {name}. Pre-travel assessments, vetted CPOs, "
        f"and secure transport across {c['areas']}."
    )[:175]

    cta_text = (
        f"Travelling to {name} for high-stakes meetings or a sensitive programme? "
        f"Request a pre-visit EP assessment."
    )

    components = [
        {
            "title": f"Pre-Travel Threat Assessment for {name}",
            "description": (
                f"Every executive protection engagement in {name} begins with a written pre-travel "
                f"threat assessment covering the current advisory ({c['advisory']}), "
                f"the threat picture derived from the {c['crime_source']}, sector-specific risks "
                f"relevant to the principal's industry context in {name}'s {c['industry_note']} sector, "
                f"and venue-by-venue security considerations across the planned itinerary."
            ),
        },
        {
            "title": f"Licensed Close Protection Officers Under {c['licensing_short']}",
            "description": (
                f"Close protection officers deployed in {name} are licensed under {c['licensing']}. "
                f"The {c['license_body']} maintains the licensing register; principals should request "
                f"confirmation of each CPO's current licence before engagement. "
                f"Vetting covers criminal records check, employment history, and relevant security training "
                f"credentials appropriate to the {name} operating environment."
            ),
        },
        {
            "title": "Secure Vehicle and Vetted Security Driver",
            "description": (
                f"EP operations in {name} integrate a vetted security driver and appropriate vehicle "
                f"as a core component of the protection detail, not an optional add-on. "
                f"The vehicle is selected for the {name} road environment: {c['transport_note']}. "
                f"Route planning is completed during the advance phase; route variation is applied across "
                f"all principal movements between {c['areas']}."
            ),
        },
        {
            "title": "Venue Advance Work",
            "description": (
                f"Venue advance for {name} EP engagements covers access and egress points at hotels, "
                f"corporate offices, and meeting venues across {c['district_note']}. "
                f"The advance officer confirms security management contact, available safe areas, "
                f"nearest medical facility (nearest: {c['hospitals'].split(';')[0]}), "
                f"and emergency service response protocol ({c['emergency']}) before the principal arrives."
            ),
        },
        {
            "title": "Operations Controller",
            "description": (
                f"A dedicated operations controller manages each EP deployment in {name} remotely, "
                f"tracking vehicle position, maintaining timed-check communication with the protection "
                f"team, and holding contingency protocols for medical emergency, route compromise, "
                f"and principal extraction. The controller is briefed on the full itinerary and "
                f"holds direct contact for {name} emergency services: {c['emergency']}."
            ),
        },
        {
            "title": "HNWI and Residential EP Options",
            "description": (
                f"For HNWI principals with a residential presence in {name}, EP options extend beyond "
                f"point-to-point corporate cover to include residential security integration, domestic "
                f"staff vetting, and recurring threat-assessment reviews for properties in "
                f"{c['res_note']}. Residential and mobile EP are coordinated under a unified security plan "
                f"rather than treated as separate contracts."
            ),
        },
    ]

    faqs = [
        {
            "question": f"What does executive protection in {name} involve in practice?",
            "answer": (
                f"EP in {name} encompasses a written pre-travel threat assessment, deployment of "
                f"licensed CPOs under {c['licensing_short']}, a vetted security driver on all vehicle "
                f"movements, venue advance work across the itinerary, and operations controller support "
                f"throughout the engagement. The threat context from the {c['crime_source']} ({c['key_threat']}) "
                f"informs route planning and situational-awareness protocols. The objective is to "
                f"reduce risk to the principal through structured, evidence-based planning, not to "
                f"provide visible security theatre."
            ),
        },
        {
            "question": f"What licensing standard applies to EP in {name}?",
            "answer": (
                f"Executive protection in {name} is regulated under {c['licensing']}. "
                f"The {c['license_body']} is the relevant authority. "
                f"Principals should request written confirmation of both the operating company's licence "
                f"and the individual CPO's registration before any engagement. "
                f"Offshore providers without local licensing carry material legal and operational risk."
            ),
        },
        {
            "question": f"What is the difference between executive protection and bodyguard hire in {name}?",
            "answer": (
                f"Executive protection in {name} is a structured security programme: threat assessment, "
                f"advance work, vehicle integration, and operations controller oversight working together. "
                f"Bodyguard hire typically refers to a single licensed CPO for close personal protection "
                f"without the full EP infrastructure. For corporate visits to {name} involving multiple "
                f"venues, international travel, or a principal with a public profile, the EP framework "
                f"provides a more appropriate standard of protection than a standalone bodyguard."
            ),
        },
        {
            "question": f"What does executive protection cost per day in {name}, as at June 2026?",
            "answer": (
                f"EP day rates in {name} for a CPO with vehicle and operations controller support range "
                f"from approximately {c['ep_day_rate']} per day, as at June 2026. "
                f"The rate varies with team size, vehicle specification, advance-work requirements, "
                f"and engagement duration. Multi-day corporate programme pricing applies a reduced "
                f"daily rate for commitments of three or more consecutive days."
            ),
        },
    ]

    threat_short_ep = c['key_threat'].split(';')[0]
    body = (
        f"{name} presents an executive protection environment defined by {threat_short_ep} "
        f"and a regulatory framework under {c['licensing_short']}. For senior executives and HNWI principals "
        f"operating across {c['district_note']}, a structured EP programme reduces the exposure that "
        f"uncoordinated travel creates. The {c['crime_source']} and current advisory ({c['advisory']}) "
        f"are the evidential baseline for every pre-travel assessment.\n"
        f"\n"
        f"## Licensing and due diligence in {name}\n"
        f"\n"
        f"All close protection officers deployed in {name} must be licensed under {c['licensing']}. "
        f"{c['unarmed_note']} The {c['license_body']} maintains the register; confirming "
        f"individual CPO licensing before engagement is standard practice, not an optional step.\n"
        f"\n"
        f"## {name} EP context: sector and threat\n"
        f"\n"
        f"{name}'s position in {c['industry_note']} creates a specific EP operating context: "
        f"principals in these sectors face both the ambient threat picture identified in the {c['crime_source']} "
        f"and sector-specific risks, including competitive intelligence activity and, for some industries, "
        f"targeted crime against high-value corporate visitors. The pre-travel assessment addresses both layers.\n"
        f"\n"
        f"For related security services in {name}, see our [{name} city page](/cities/{city_slug}/), "
        f"[security drivers in {name}](/security-drivers/{city_slug}/), "
        f"and [bodyguard hire in {name}](/bodyguard-hire/{city_slug}/)."
    )

    return _render_page(
        title=title, description=description, slug=city_slug, h1=h1,
        seo_title=seo_title, service="executive-protection", city=name,
        country=country, risk_level=c["risk_level"], hero_image=c["hero_image"],
        cta_text=cta_text, components=components, faqs=faqs, body=body,
    )


def gen_residential_security(city_slug, c):
    name = c["name"]
    country = c["country"]
    seo_title = f"Residential Security {name} | {country} Home Protection"
    if len(seo_title) > 70:
        seo_title = f"Residential Security {name} | Home Protection"

    title = f"Residential Security in {name}"
    h1 = f"Residential Security Services in {name}, {country}"
    description = (
        f"Licensed residential security in {name}. Property assessments, manned guarding, "
        f"and staff vetting for HNWI principals in {c['areas']}."
    )[:175]

    cta_text = (
        f"Own or lease a property in {name}? "
        f"Request a residential security assessment from a licensed provider."
    )

    components = [
        {
            "title": "Property Security Assessment",
            "description": (
                f"Every residential security engagement in {name} starts with a written property "
                f"assessment covering perimeter integrity, access control, CCTV and alarm provision, "
                f"safe room adequacy, and the specific threat profile relevant to the property location "
                f"within {c['areas']}. The assessment is benchmarked against the {c['crime_source']} "
                f"threat picture and produces a prioritised remediation schedule."
            ),
        },
        {
            "title": f"Manned Guarding Under {c['licensing_short']}",
            "description": (
                f"Manned guarding officers deployed at residential properties in {name} are licensed "
                f"under {c['licensing']}. The {c['license_body']} maintains the register. "
                f"Guard rosters are structured to avoid predictable shift patterns; post orders "
                f"are written specifically to the property layout and access control configuration "
                f"rather than adapted from generic templates."
            ),
        },
        {
            "title": "Alarm and Response Integration",
            "description": (
                f"Residential security in {name} integrates the property's electronic security "
                f"systems, including intruder alarm, CCTV, and smart access control, with a "
                f"monitored alarm receiving centre and a vetted physical response resource. "
                f"Response times to {c['res_note']} from a properly resourced monitoring centre "
                f"are assessed during the initial property review and benchmarked against local "
                f"police response data."
            ),
        },
        {
            "title": "Domestic Staff Vetting",
            "description": (
                f"Domestic staff represent a significant access-control vulnerability in residential "
                f"security in {name}. Vetting for household staff covers criminal records check, "
                f"employment and identity verification, and where legally available, adverse media "
                f"screening. The vetting standard is documented, retained, and renewed on a periodic "
                f"cycle aligned to tenure. This applies to all staff with regular unsupervised access "
                f"to the property."
            ),
        },
        {
            "title": "Safe Room and Shelter Planning",
            "description": (
                f"For HNWI residential properties in {name}, safe room or hardened shelter provision "
                f"is assessed during the property review. Requirements depend on the assessed threat: "
                f"{c['key_threat'].split(';')[0]}. A safe room specification covers communications, "
                f"duration of shelter provision, access control independent of the main property "
                f"system, and coordination protocol with {name} emergency services ({c['emergency']})."
            ),
        },
        {
            "title": "Recurring Security Audit",
            "description": (
                f"Residential security in {name} is not a one-time installation: threats evolve, "
                f"household composition changes, and the local crime picture shifts. A recurring "
                f"security audit on an agreed schedule, typically quarterly or after any significant "
                f"incident in {c['areas']}, ensures the security posture remains appropriate "
                f"to current conditions and does not degrade through familiarity or staff turnover."
            ),
        },
    ]

    faqs = [
        {
            "question": f"What are the most common gaps in residential security for properties in {name}?",
            "answer": (
                f"The {c['crime_source']} identifies {c['key_threat']}. In residential settings in "
                f"{name}, the most common security gaps are: inadequate access control at perimeter "
                f"points, CCTV blind spots at side and rear elevations, unvetted or under-vetted "
                f"domestic staff, and alarm systems that are not connected to a monitored receiving "
                f"centre. A written property assessment identifies and prioritises these gaps before "
                f"any remediation work is commissioned."
            ),
        },
        {
            "question": f"Do I need manned guarding for my {name} property?",
            "answer": (
                f"Manned guarding is not appropriate for every residential property in {name}. "
                f"The decision depends on the assessed threat level for the location, the principal's "
                f"profile, the physical characteristics of the property, and the adequacy of electronic "
                f"security measures already in place. The property security assessment produces a "
                f"recommendation based on these factors rather than a default recommendation for "
                f"guarding, which is a significant and recurring cost commitment."
            ),
        },
        {
            "question": f"How is domestic staff vetting conducted in {name}?",
            "answer": (
                f"Domestic staff vetting in {name} covers criminal records check through the relevant "
                f"national system, identity verification, employment history verification, and adverse "
                f"media screening. The vetting is documented and retained by the security provider. "
                f"Temporary and agency staff require the same vetting standard as permanent household "
                f"employees; vetting should be renewed on contract renewal and periodically for "
                f"long-tenure staff."
            ),
        },
        {
            "question": f"What does residential security cost per month in {name}, as at June 2026?",
            "answer": (
                f"Residential security costs in {name} vary significantly based on the level of service: "
                f"an initial property assessment followed by electronic security upgrades may be a "
                f"one-time cost, while a manned guarding contract typically ranges from "
                f"{c['rs_month_rate']}, as at June 2026, depending on post hours, guard specification, "
                f"and response requirements. A costed security plan is produced following the "
                f"initial property assessment."
            ),
        },
    ]

    import re as _re
    threat_short = c['key_threat'].split(';')[0]
    # Strip trailing parenthetical source citation from threat_short to avoid duplication
    threat_short_clean = _re.sub(r'\s*\([^)]*\)\s*$', '', threat_short).strip()
    # Also strip leading "SourceName: " prefix if it matches crime_source
    crime_src_prefix = c['crime_source'] + ': '
    if threat_short_clean.startswith(crime_src_prefix):
        threat_short_clean = threat_short_clean[len(crime_src_prefix):]
    hosp_first = c['hospitals'].split(';')[0]
    body = (
        f"Residential security in {name} addresses the specific threat context identified in the "
        f"{c['crime_source']}: {threat_short_clean}. For HNWI principals and senior executives "
        f"with residential properties in {c['res_note']}, a structured residential security programme "
        f"provides measurably more protection than ad hoc or uncoordinated measures. All guarding "
        f"personnel are licensed under {c['licensing_short']} and vetted to a documented standard.\n"
        f"\n"
        f"## Property assessment as the foundation\n"
        f"\n"
        f"A written property security assessment is the non-negotiable starting point for residential "
        f"security in {name}. It identifies the specific vulnerabilities at the subject property, "
        f"benchmarks them against the local threat picture, and produces a prioritised remediation schedule. "
        f"A security provider that recommends a guarding contract without a prior written assessment has "
        f"inverted the correct sequence.\n"
        f"\n"
        f"## {c['res_note']}: operating environment\n"
        f"\n"
        f"Residential areas in {name}, including {c['res_note']}, have distinct access patterns, "
        f"neighbour density characteristics, and local police response capabilities that affect "
        f"the appropriate security design. Electronic integration with a monitored receiving centre, "
        f"staff vetting, and periodic audit are the three measures that deliver the most consistent "
        f"protective value for residential principals in {name}.\n"
        f"\n"
        f"For wider security services in {name}, see our [{name} city page](/cities/{city_slug}/) "
        f"and [executive protection in {name}](/executive-protection/{city_slug}/) "
        f"and [bodyguard hire in {name}](/bodyguard-hire/{city_slug}/)."
    )

    return _render_page(
        title=title, description=description, slug=city_slug, h1=h1,
        seo_title=seo_title, service="residential-security", city=name,
        country=country, risk_level=c["risk_level"], hero_image=c["hero_image"],
        cta_text=cta_text, components=components, faqs=faqs, body=body,
    )


def gen_event_security(city_slug, c):
    name = c["name"]
    country = c["country"]
    seo_title = f"Event Security {name} | {country} Corporate Events"
    if len(seo_title) > 70:
        seo_title = f"Event Security {name} | Corporate Event Security"

    title = f"Event Security in {name}"
    h1 = f"Event Security Services in {name}, {country}"
    description = (
        f"Licensed event security in {name}. Venue assessments, VIP close protection, "
        f"access control, and emergency planning for corporate events."
    )[:175]

    cta_text = (
        f"Planning a corporate or high-profile event in {name}? "
        f"Request an event security assessment from a licensed provider."
    )

    components = [
        {
            "title": "Venue Security Assessment",
            "description": (
                f"Event security in {name} begins with a written venue security assessment covering "
                f"access and egress points, CCTV coverage, crowd-density calculations for the "
                f"planned attendance, and emergency evacuation routing. Major event venues in {name} "
                f"include {c['event_note']}. Assessments identify venue-specific gaps before the "
                f"event security plan is finalised."
            ),
        },
        {
            "title": "Close Protection for Principals and VIPs",
            "description": (
                f"Named VIPs and executive principals attending events in {name} require individual "
                f"close protection plans distinct from the general event security overlay. "
                f"CPOs licensed under {c['licensing_short']} are assigned to VIP principals; "
                f"advance work covers arrival protocols, designated safe areas within the venue, "
                f"and discreet extraction routing if the principal needs to depart early or under pressure."
            ),
        },
        {
            "title": "Access Control",
            "description": (
                f"Access control for corporate events in {name} operates on a tiered credentialling "
                f"system: public perimeter, delegate registration, and VIP/principal zone. "
                f"Credentialling staff are licensed under {c['licensing_short']}. "
                f"Physical access control is supported by CCTV monitoring at all perimeter points "
                f"and a radio communication net connecting access teams with the event security manager."
            ),
        },
        {
            "title": "Event Transport and Secure Transfer",
            "description": (
                f"Transport logistics for events in {name} are planned as part of the overall security "
                f"design, not organised separately. Vetted security drivers on pre-planned routes "
                f"reduce the predictability that event vehicle staging creates, particularly at high-profile "
                f"events where the arrival and departure of principals is publicly visible. "
                f"Transfer routes across {c['transport_note']} are risk-assessed before the event."
            ),
        },
        {
            "title": "Crowd and Venue-Space Awareness",
            "description": (
                f"Events in {name} with significant public attendance require structured crowd-awareness "
                f"protocols informed by the venue layout and local emergency services guidance. "
                f"The {c['crime_source']} provides the ambient context; event-specific crowd-management "
                f"planning addresses flow management at entry and exit, identification of potential "
                f"flash-point zones, and liaison with {name} police and venue management."
            ),
        },
        {
            "title": "Emergency Response Planning",
            "description": (
                f"Every event security plan for {name} includes a written emergency response protocol: "
                f"medical emergency (nearest hospital: {c['hospitals'].split(';')[0]}), "
                f"security incident, and full evacuation. Emergency services contact: {c['emergency']}. "
                f"The protocol is briefed to all security personnel before the event, includes rally "
                f"points and communication cascade, and is coordinated with venue management and, "
                f"where appropriate, local police liaison."
            ),
        },
    ]

    faqs = [
        {
            "question": f"Is {name} suitable for high-profile corporate events from a security standpoint?",
            "answer": (
                f"{name} is an established corporate event destination with a well-developed venue "
                f"infrastructure including {c['event_note']}. The current advisory is: {c['advisory']}. "
                f"The {c['crime_source']} identifies: {c['key_threat']}. With appropriate venue selection, "
                f"licensed event security personnel, and a written emergency response plan, {name} "
                f"supports a wide range of corporate and HNWI event formats. A pre-event threat "
                f"assessment provides an evidence-based foundation for the security design."
            ),
        },
        {
            "question": f"How does venue selection affect event security planning in {name}?",
            "answer": (
                f"Venue selection is the single largest determinant of event security complexity in {name}. "
                f"Established corporate venues such as {c['event_note']} hold existing security "
                f"infrastructure, established emergency protocols, and dedicated security management. "
                f"Non-standard or non-purpose-built venues require a more extensive written assessment "
                f"before the event security plan can be finalised. Venue access and egress are the "
                f"primary factors: restricted access options and limited egress create the most "
                f"significant crowd-safety and emergency-response risk."
            ),
        },
        {
            "question": f"What licensing standard applies to event security personnel in {name}?",
            "answer": (
                f"Event security personnel in {name} must be licensed under {c['licensing']}. "
                f"The {c['license_body']} is the relevant registration authority. "
                f"SIA Door Supervisor or equivalent local licence is the standard for access control "
                f"and venue perimeter roles; CPO-licensed personnel are required for named VIP "
                f"close protection. Principals should request a licence schedule from the event "
                f"security provider confirming the credentials of all deployed personnel."
            ),
        },
        {
            "question": f"What emergency planning is required for a corporate event in {name}?",
            "answer": (
                f"Emergency planning for a corporate event in {name} must cover at minimum: medical "
                f"emergency response (nearest hospital: {c['hospitals'].split(';')[0]}; "
                f"emergency services: {c['emergency']}), general evacuation routing from the venue, "
                f"communication cascade between security teams and venue management, and a protocol "
                f"for coordinating with local police if required. The emergency plan is briefed to "
                f"all security personnel before the event and rehearsed at venue walk-through stage."
            ),
        },
    ]

    threat_short_es = c['key_threat'].split(';')[0]
    body = (
        f"{name} is a major corporate event destination, hosting events at {c['event_note']}. "
        f"Event security in {name} is regulated under {c['licensing_short']}, requiring all deployed "
        f"personnel to hold current licences from the {c['license_body']}. The threat context from the "
        f"{c['crime_source']} ({threat_short_es}) informs both venue selection guidance "
        f"and the emergency response protocols built into every event security plan.\n"
        f"\n"
        f"## Venue assessment and access control\n"
        f"\n"
        f"A written venue security assessment is the starting point for any event security engagement in "
        f"{name}. The assessment addresses access and egress constraints, CCTV coverage, crowd-density "
        f"planning for the planned attendance, and emergency evacuation routing. Access control operates "
        f"on a tiered credentialling system with licensed personnel at all perimeter points.\n"
        f"\n"
        f"## VIP protection and transport integration\n"
        f"\n"
        f"Named principals and VIPs attending events in {name} require individual close protection plans "
        f"integrated with the overall event security structure. Security drivers on pre-planned routes "
        f"coordinate arrival and departure with the event security manager to reduce the exposure that "
        f"predictable vehicle staging creates.\n"
        f"\n"
        f"For related security services in {name}, see our [{name} city page](/cities/{city_slug}/) "
        f"and [/services/event-security/](/services/event-security/) "
        f"and [bodyguard hire in {name}](/bodyguard-hire/{city_slug}/)."
    )

    return _render_page(
        title=title, description=description, slug=city_slug, h1=h1,
        seo_title=seo_title, service="event-security", city=name,
        country=country, risk_level=c["risk_level"], hero_image=c["hero_image"],
        cta_text=cta_text, components=components, faqs=faqs, body=body,
    )


def gen_close_protection_officers(city_slug, c):
    name = c["name"]
    country = c["country"]
    seo_title = f"Close Protection Officers {name} | {c['license_body']}"
    if len(seo_title) > 70:
        seo_title = f"Close Protection Officers {name} | Licensed CPOs"

    title = f"Close Protection Officers in {name}"
    h1 = f"Close Protection Officers in {name}, {country}"
    description = (
        f"Licensed close protection officers in {name}. Vetted CPOs for corporate, "
        f"HNWI, and event deployments across {c['areas']}."
    )[:175]

    cta_text = (
        f"Require a licensed CPO for a visit or programme in {name}? "
        f"Request a vetted close protection officer."
    )

    components = [
        {
            "title": f"Licensing Standard: {c['licensing_short']}",
            "description": (
                f"Close protection officers operating in {name} must be licensed under {c['licensing']}. "
                f"The {c['license_body']} maintains the licensing register. "
                f"Licence verification is the first due-diligence step when appointing a CPO in {name}: "
                f"the operating company's registration and the individual officer's personal licence "
                f"should both be confirmed in writing before deployment. Unlicensed operators carry "
                f"legal and reputational risk for the engaging principal."
            ),
        },
        {
            "title": f"Threat Assessment and Operational Planning for {name}",
            "description": (
                f"CPO deployment in {name} is preceded by a written threat assessment covering "
                f"the current advisory ({c['advisory']}), the {c['crime_source']} threat picture "
                f"({c['key_threat']}), and the specific exposure points in the principal's "
                f"planned itinerary across {c['areas']}. The assessment determines the level of "
                f"protection required, the profile of CPO most appropriate (high-visibility versus "
                f"low-profile), and the vehicle and advance-work requirements."
            ),
        },
        {
            "title": "Armed and Unarmed Options",
            "description": (
                f"{c['armed_note']} {c['unarmed_note']} The determination of armed versus unarmed "
                f"is made on the basis of the written threat assessment, not by default. In almost all "
                f"corporate and HNWI engagement types in {name}, unarmed close protection is the "
                f"appropriate operational standard, with armed options reserved for specific "
                f"assessed threats."
            ),
        },
        {
            "title": "Venue Advance Work",
            "description": (
                f"The CPO or an advance officer conducts physical venue reconnaissance at hotels, "
                f"corporate offices, and meeting venues across {c['district_note']} before the "
                f"principal's arrival. Advance work confirms access and egress routes, safe area "
                f"availability, nearest medical resource ({c['hospitals'].split(';')[0]}), "
                f"and emergency services contact ({c['emergency']}). "
                f"The advance report is shared with the operations controller before principal movement begins."
            ),
        },
        {
            "title": "Operations Controller Support",
            "description": (
                f"Every CPO deployment in {name} is supported by a remote operations controller "
                f"maintaining timed-check communication with the deployed officer, tracking vehicle "
                f"movements, and holding contingency protocols for security incident, medical emergency, "
                f"and principal extraction. The controller is the coordination hub between the CPO, "
                f"the security driver, and any venue security management."
            ),
        },
        {
            "title": "Transport Integration",
            "description": (
                f"Close protection in {name} is most effective when the CPO and security driver "
                f"operate as an integrated team under a unified security plan. The CPO briefs the "
                f"driver on principal movement timings, venue access protocols, and contingency "
                f"routes. Transport integration is particularly important on {c['transport_note']}, "
                f"where traffic conditions and the specific threat picture in {name} make route "
                f"variation a material protective measure."
            ),
        },
    ]

    faqs = [
        {
            "question": f"What licence does a close protection officer need to operate in {name}?",
            "answer": (
                f"CPOs operating in {name} must be licensed under {c['licensing']}. "
                f"The relevant authority is the {c['license_body']}. "
                f"The individual CPO must hold a current personal licence; the operating company "
                f"must hold the appropriate commercial security licence. "
                f"Both should be confirmed in writing before any CPO is deployed. "
                f"Licence status can be verified through the {c['license_body']}."
            ),
        },
        {
            "question": f"What is the distinction between a close protection officer and a bodyguard in {name}?",
            "answer": (
                f"In {name}, as in most markets, the terms are often used interchangeably. "
                f"A close protection officer is the formal, licensed designation under {c['licensing_short']}; "
                f"bodyguard is the common description. Operationally, a professionally deployed CPO "
                f"in {name} integrates advance work, threat assessment, vehicle coordination, and "
                f"operations controller support into the protective role, rather than providing "
                f"only a physical presence alongside the principal. The licensed term is CPO; "
                f"the quality benchmark is the integrated EP programme."
            ),
        },
        {
            "question": f"How is the armed or unarmed decision made for CPO deployments in {name}?",
            "answer": (
                f"The armed/unarmed decision is made on the basis of the written threat assessment "
                f"for the specific engagement in {name}, not by default. {c['armed_note']} "
                f"For the overwhelming majority of corporate, HNWI, and event deployments in {name}, "
                f"unarmed close protection is the appropriate and legally straightforward option. "
                f"Armed options are reserved for specific assessed threats and require engagement "
                f"with operators who hold the relevant authorisations under {c['licensing_short']}."
            ),
        },
        {
            "question": f"What does a close protection officer cost per day in {name}, as at June 2026?",
            "answer": (
                f"CPO day rates in {name} range from approximately {c['cpo_day_rate']} per day, "
                f"as at June 2026, depending on individual experience, licensing level, and "
                f"engagement type. Multi-day corporate programme rates apply a reduced daily rate "
                f"for three or more consecutive days. Vehicle and operations controller costs are "
                f"typically quoted separately; a combined EP package rate is available on request."
            ),
        },
    ]

    threat_short_cpo = c['key_threat'].split(';')[0]
    body = (
        f"Close protection officers operating in {name} are licensed under {c['licensing']}, "
        f"with the {c['license_body']} maintaining the registration register. "
        f"For corporate executives, HNWI principals, and event organisers requiring vetted CPOs in {name}, "
        f"the licensing framework is the starting point for due diligence. The {c['crime_source']} "
        f"({threat_short_cpo}) informs the threat assessment that precedes every CPO deployment.\n"
        f"\n"
        f"## Licensing and due diligence\n"
        f"\n"
        f"Confirming the individual CPO's personal licence and the operating company's registration with "
        f"the {c['license_body']} is a non-negotiable first step. Overseas providers without local "
        f"licensing carry legal and operational risk that the engaging principal inherits. "
        f"{c['unarmed_note']}\n"
        f"\n"
        f"## CPOs in {name}: operational context\n"
        f"\n"
        f"CPO deployments in {name} cover {c['district_note']} and the principal movement corridors "
        f"across {c['transport_note']}. Venue advance work, operations controller integration, "
        f"and transport coordination with a vetted security driver are the components that distinguish "
        f"a professional CPO engagement from a standalone hired presence.\n"
        f"\n"
        f"For related security services in {name}, see our [{name} city page](/cities/{city_slug}/), "
        f"[bodyguard hire in {name}](/bodyguard-hire/{city_slug}/), "
        f"and [executive protection in {name}](/executive-protection/{city_slug}/)."
    )

    return _render_page(
        title=title, description=description, slug=city_slug, h1=h1,
        seo_title=seo_title, service="close-protection-officers", city=name,
        country=country, risk_level=c["risk_level"], hero_image=c["hero_image"],
        cta_text=cta_text, components=components, faqs=faqs, body=body,
    )


# ---------------------------------------------------------------------------
# YAML renderer
# ---------------------------------------------------------------------------

def _yaml_str(value):
    """Wrap a string in YAML double quotes, escaping internal double quotes."""
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def _render_page(*, title, description, slug, h1, seo_title, service, city,
                 country, risk_level, hero_image, cta_text, components, faqs, body):
    """Render a Hugo content page as a YAML-fronted Markdown string."""
    lines = ["---"]
    lines.append(f"title: {_yaml_str(title)}")
    lines.append(f"description: {_yaml_str(description)}")
    lines.append(f"slug: {_yaml_str(slug)}")
    lines.append(f"h1: {_yaml_str(h1)}")
    lines.append(f"seo_title: {_yaml_str(seo_title)}")
    lines.append(f"service: {_yaml_str(service)}")
    lines.append(f"city: {_yaml_str(city)}")
    lines.append(f"country: {_yaml_str(country)}")
    lines.append(f"risk_level: {_yaml_str(risk_level)}")
    lines.append(f"hero_image: {_yaml_str(hero_image)}")
    lines.append('date: "2026-06-18"')
    lines.append(f"cta_text: {_yaml_str(cta_text)}")
    lines.append("components:")
    for comp in components:
        lines.append(f"  - title: {_yaml_str(comp['title'])}")
        lines.append(f"    description: {_yaml_str(comp['description'])}")
    lines.append("faqs:")
    for faq in faqs:
        lines.append(f"  - question: {_yaml_str(faq['question'])}")
        lines.append(f"    answer: {_yaml_str(faq['answer'])}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# QA checks
# ---------------------------------------------------------------------------

EM_DASH = "—"
SAFETY_GUARANTEE_PATTERNS = [
    "guarantee safety", "100% safe", "keep you safe", "risk-free",
    "risk free", "foolproof", "bulletproof security",
]


def qa_check(content, filepath):
    errors = []
    if EM_DASH in content:
        errors.append("Contains em dash")
    for pat in SAFETY_GUARANTEE_PATTERNS:
        if pat.lower() in content.lower():
            errors.append(f"Safety guarantee pattern: '{pat}'")
    # Count internal links (relative URLs)
    import re
    links = re.findall(r'\]\(/', content)
    if len(links) < 2:
        errors.append(f"Only {len(links)} internal link(s) found; minimum 2 required")
    # Check description length
    m = re.search(r'^description:\s*"(.*?)"', content, re.MULTILINE)
    if m:
        desc = m.group(1)
        if len(desc) < 120 or len(desc) > 175:
            errors.append(f"Description length {len(desc)} chars (expected 120-175)")
    # Check seo_title length
    m = re.search(r'^seo_title:\s*"(.*?)"', content, re.MULTILINE)
    if m:
        st = m.group(1)
        if len(st) > 70:
            errors.append(f"seo_title too long: {len(st)} chars")
    # Count FAQs
    faq_count = content.count("  - question:")
    if faq_count < 4:
        errors.append(f"Only {faq_count} FAQs found; minimum 4 required")
    # Count components: components use "  - title:", FAQs use "  - question:"
    comp_count = content.count("  - title:")
    if comp_count < 6:
        errors.append(f"Only {comp_count} components found; minimum 6 required")
    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

SERVICE_GENERATORS = {
    "security-drivers": gen_security_drivers,
    "executive-protection": gen_executive_protection,
    "residential-security": gen_residential_security,
    "event-security": gen_event_security,
    "close-protection-officers": gen_close_protection_officers,
}


def main():
    created = 0
    skipped = 0
    qa_failures = []

    for service in SERVICES:
        service_dir = CONTENT_DIR / service
        service_dir.mkdir(parents=True, exist_ok=True)

        generator = SERVICE_GENERATORS[service]

        for city_slug in CITY_ORDER:
            city_data = CITIES[city_slug]
            out_path = service_dir / f"{city_slug}.md"

            # Generate content
            content = generator(city_slug, city_data)

            # QA check
            errors = qa_check(content, out_path)
            if errors:
                print(f"  QA FAIL [{service}/{city_slug}]: {'; '.join(errors)}")
                qa_failures.append((service, city_slug, errors))
                skipped += 1
                continue

            # Write file
            out_path.write_text(content, encoding="utf-8")
            print(f"  Created: {out_path.relative_to(BASE_DIR)}")
            created += 1

    print()
    print("=" * 60)
    print(f"Pages created : {created}")
    print(f"Pages skipped : {skipped} (QA failures)")
    if qa_failures:
        print()
        print("QA failure details:")
        for service, city_slug, errors in qa_failures:
            print(f"  {service}/{city_slug}: {'; '.join(errors)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
