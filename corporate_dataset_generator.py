import csv
import random
from datetime import datetime, timedelta

#lista di aziende
clients = [
    "Siemens", "Volkswagen", "BMW", "Daimler", "Bosch", "Allianz", "Deutsche Telekom", "SAP",
   "Unilever", "Royal Dutch Shell", "ING Group", "Philips", "Heineken", "AXA", "Total",
   "L'Oréal", "Renault", "Airbus", "Sanofi", "Orange", "Nestlé", "Credit Suisse", "Novartis",
   "UBS", "ABB", "Glencore", "HSBC", "BP", "Barclays", "Vodafone", "Rolls-Royce", "GlaxoSmithKline",
   "Rio Tinto", "Tesco", "Prudential", "Lloyds Banking Group", "Aviva", "BNP Paribas", "Michelin",
   "Alstom", "Veolia", "Société Générale", "LVMH", "Danone", "EDF", "Thales Group", "Telefónica",
   "Iberdrola", "Repsol", "Inditex", "BBVA", "Banco Santander", "Eni", "Enel", "Stellantis",
   "Generali Group", "Intesa Sanpaolo", "UniCredit", "Pirelli", "Leonardo S.p.A.", "Volvo", "Ericsson",
   "IKEA", "H&M", "Electrolux", "Nordea", "Maersk", "Novo Nordisk", "Carlsberg", "Vestas",
   "ArcelorMittal", "Solvay", "KBC Group", "UCB", "Demant", "LEGO Group", "Vattenfall",
   "AstraZeneca", "BT Group", "EasyJet", "Kingfisher", "Marks & Spencer", "Next", "Sainsbury's",
   "EDF Energy", "National Grid", "Telenor", "Nokia", "Fortum", "Outokumpu", "Stora Enso",
   "Ferrovial", "ACS Group", "Amadeus IT Group", "Mapfre", "Sabadell", "Cepsa", "OMV Group",
   "Raiffeisen Bank", "Erste Group", "Strabag", "DNB ASA", "Yara International", "Orkla",
   "Alfa Laval", "Sandvik", "Skanska", "SKF", "Tele2", "Telia Company", "Zurich Insurance Group",
   "Holcim", "Swiss Re", "Lonza Group", "Clariant", "Sika AG", "ABB Ltd", "Lindt & Sprüngli",
   "Roche", "Wolseley", "Imperial Brands", "Compass Group", "Relx Group", "Melrose Industries",
   "Schneider Electric", "Saint-Gobain", "Capgemini", "Safran", "Vivendi", "Kering", "Amundi",
   "Assicurazioni Generali", "Poste Italiane", "Telecom Italia", "Atlantia", "Fincantieri", "Terna",
   "Enagas", "Red Eléctrica", "Aena", "Ryanair", "CRH plc", "Smurfit Kappa", "Kerry Group",
   "Glanbia", "Kingspan Group", "Ferrero", "Barilla", "Bayer", "Continental AG", "Deutsche Bank",
   "Fiat", "Porsche", "Lufthansa", "Coca-Cola HBC", "E.ON", "METRO AG", "BASF", "AkzoNobel",
   "Fresenius", "Henkel", "Merck Group", "Osram", "Puma", "Adidas", "ThyssenKrupp",
   "HeidelbergCement", "Evonik", "Zalando", "Delivery Hero", "Air Liquide", "Pernod Ricard",
   "Eiffage", "JCDecaux", "Bouygues", "Accor", "EssilorLuxottica", "Valeo", "Dassault Systèmes",
   "Engie", "EDP", "Galp Energia", "Jerónimo Martins", "Bankia", "Abertis", "Grifols", "Cellnex",
   "Balfour Beatty", "BAE Systems", "Diageo", "Experian", "GSK", "ITV plc", "Legal & General",
   "London Stock Exchange Group", "Reckitt Benckiser", "Standard Chartered", "WPP plc", "Centrica",
   "Kingfisher plc", "Morrison Supermarkets", "Rolls-Royce Holdings", "Aegon", "ASML Holding",
   "DSM", "Randstad Holding", "Ageas", "Barco", "Euroclear", "Argenta", "Mediaset", "Moncler",
   "Prada", "Snam", "Ferrari", "Legrand", "LafargeHolcim", "Publicis Groupe", "STMicroelectronics",
   "Suez", "Givaudan", "Richemont", "Sika AG", "Swatch Group", "Nestlé", "Adecco Group",
   "Kuehne + Nagel", "Logitech", "Sonova", "Straumann", "Swisscom", "Temenos AG", "Burberry",
   "BHP", "DCC plc", "Glanbia", "Greencore", "Paddy Power Betfair", "CRH plc", "Banco Comercial Português",
   "Mota-Engil", "Sonae", "Anheuser-Busch InBev", "Proximus", "Bpost", "Belgacom", "Recticel",
   "Bekaert", "Delhaize Group", "Umicore", "KBC Group", "Atlas Copco", "Securitas AB", "Ferrovial",
   "Grupo ACS", "CaixaBank", "Gas Natural", "Acerinox", "Acciona", "Endesa", "Enagas", "Mapfre",
   "Iberdrola", "Sacyr", "NH Hotel Group", "Vidrala", "Viscofan", "Zardoya Otis", "Atresmedia",
   "Mediaset España", "Euskaltel", "Alantra Partners", "Talgo", "Admiral Group", "Just Eat",
   "Rightmove", "Legal & General", "Aviva", "Phoenix Group", "Scottish Mortgage Investment Trust",
   "British Land", "Land Securities", "Segro", "Hammerson", "Derwent London", "Great Portland Estates",
   "Unite Group", "Blackstone Group", "CBRE Group", "Knight Frank", "Savills", "Greene King",
   "Whitbread", "Marston's", "JD Wetherspoon", "Mitchells & Butlers", "Rank Group", "William Hill",
   "GVC Holdings", "888 Holdings", "Playtech", "Flutter Entertainment", "Betsson", "Kindred Group",
   "Zurich Insurance Group", "ABB", "Straumann", "Swatch Group", "Lindt & Sprüngli", "DNB ASA",
   "Equinor", "Fortum", "Neste", "UPM-Kymmene", "Kone", "Wärtsilä", "Kesko", "Aker BP", "Storebrand",
   "Swedbank", "SEB Group", "Atlas Copco", "Volvo Group", "Electrolux", "Boliden", "Assa Abloy",
   "Getinge", "SSAB", "E.ON", "Deutsche Börse", "Porsche SE", "Commerzbank", "MAN SE", "Beiersdorf",
   "Fraport", "K+S AG", "MTU Aero Engines", "Sartorius", "Cancom", "Software AG", "Andritz AG",
   "Voestalpine", "Vienna Insurance Group", "RHI Magnesita", "AMS AG", "Bawag Group", "Geberit",
   "Barry Callebaut", "Clariant", "Galenica", "Burberry", "Coca-Cola European Partners",
   "Kingspan Group", "Euskaltel", "Coca-Cola HBC", "Aviva", "Nestlé", "Novartis", "Roche",
   "Holcim", "Lonza Group", "UBS", "Swatch Group", "Givaudan", "Sika AG", "ABB", "Adecco Group",
   "Swisscom", "Nestlé", "Kuehne + Nagel", "DSM", "ASML Holding", "Heineken", "ING Group",
   "Ahold Delhaize", "Koninklijke Philips", "AkzoNobel", "NN Group", "Vopak", "TNT Express",
   "Randstad Holding", "TomTom", "Altice Europe", "Fugro", "Boskalis Westminster", "Van Oord",
   "Arcadis", "Royal BAM Group", "Ballast Nedam", "Arcadis", "An Post", "Bord na Móna",
   "Cairn Homes", "CRH plc", "Glanbia", "Kerry Group", "Kingspan Group", "Paddy Power Betfair",
   "Ryanair", "A.P. Møller – Mærsk", "Carlsberg Group", "Danske Bank", "ISS A/S", "Novo Nordisk",
   "Novozymes", "Pandora", "Tryg", "Coloplast", "GN Store Nord", "Vestas", "William Demant",
   "Ørsted", "Admiral Group", "Anglo American", "Antofagasta", "Ashtead Group", "Associated British Foods",
   "Auto Trader Group", "Aviva", "Babcock International Group", "Bae Systems", "Barclays", "Barratt Developments",
   "Berkeley Group Holdings", "BP", "British American Tobacco", "BT Group", "Bunzl", "Carnival Corporation & plc",
   "Centrica", "Compass Group", "Croda International", "Diageo", "Evraz", "Experian", "Ferguson plc",
   "Flutter Entertainment", "Fresnillo", "GlaxoSmithKline", "Glencore", "Hikma Pharmaceuticals", "HSBC Holdings",
   "Imperial Brands", "Informa", "InterContinental Hotels Group", "International Airlines Group", "Intertek Group",
   "ITV plc", "JD Sports Fashion", "Johnson Matthey", "Just Eat Takeaway", "Kingfisher plc", "Land Securities",
   "Legal & General", "Lloyds Banking Group", "London Stock Exchange Group", "M&G", "Melrose Industries", "Mondi",
   "National Grid plc", "Next plc", "Ocado Group", "Pearson plc", "Persimmon plc", "Phoenix Group Holdings", "Prudential plc",
   "Reckitt Benckiser", "RELX", "Rentokil Initial", "Rio Tinto", "Rolls-Royce Holdings", "Royal Dutch Shell", "RSA Insurance Group",
   "Sage Group", "Sainsbury's", "Schroders", "Scottish Mortgage Investment Trust", "Segro", "Severn Trent", "Smith & Nephew",
   "Smiths Group", "Smurfit Kappa", "Spirax-Sarco Engineering", "SSE plc", "St. James's Place plc", "Standard Chartered",
   "Taylor Wimpey", "Tesco", "Unilever", "United Utilities", "Vodafone Group", "Whitbread", "WPP plc"
]

# paesi europei
countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia",
    "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland",
    "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia",
    "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom",
    "Vatican City"
]

# metodi di pagamento
payment_methods = ["credit_card", "cash", "debit_card"]

# generare numero arbitrario di righe (date 2023)
rows = []
start_date = datetime(2023, 1, 1)
for _ in range(21_113):
    client = random.choice(clients)
    date_of_purchase = (start_date + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d')
    units = random.randint(1, 100)
    price_per_unit = round(random.uniform(10.0, 300.0), 2)
    payment_method = random.choice(payment_methods)
    payment_hour = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"
    country = random.choice(countries)
    rows.append([client, date_of_purchase, units, price_per_unit, payment_method, payment_hour, country])

# output csv
with open('corporate_purchase.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
   
    writer.writerow(["client", "date_of_purchase", "units", "price_per_unit", "payment_method", "payment_hour", "country"])
    writer.writerows(rows)

print("Dataset successfully generated in the file 'corporate_purchase.csv'.")
