import sqlite3

# Connect to a new database (or open an existing one)
conn = sqlite3.connect('india_trade.db')

# Create a new table for export commodities
conn.execute('''CREATE TABLE IF NOT EXISTS exports (
                commodity TEXT PRIMARY KEY,
                value REAL
            )''')

# Insert data into exports table
exports_data = [('Petroleum Products', 21.20),
                ('Gems & Jewellery', 17.70),
                ('Drug Formulations, Biologicals', 15.70),
                ('Cotton Yarn/Fabrics/Made-ups, Handloom Products etc.', 5.30),
                ('Organic & Inorganic Chemicals', 5.20),
                ('Engineering Goods', 4.40),
                ('Electronic Goods', 3.90),
                ('Rice', 3.60),
                ('Meat, Dairy & Poultry Products', 1.90),
                ('Plastics & Linoleum', 1.80)]
conn.executemany('INSERT INTO exports (commodity, value) VALUES (?, ?)', exports_data)

# Create a new table for import commodities
conn.execute('''CREATE TABLE IF NOT EXISTS imports (
                commodity TEXT PRIMARY KEY,
                value REAL
            )''')

# Insert data into imports table
imports_data = [('Crude Oil', 61.08),
                ('Natural Gas', 5.61),
                ('Pearls, precious & Semi-precious stones', 3.92),
                ('Electronic Goods', 3.31),
                ('Gold', 2.59),
                ('Petroleum Products', 2.41),
                ('Coal, Coke & Briquettes', 1.83),
                ('Chemicals (Organic/Inorganic)', 1.79),
                ('Iron & Steel', 1.48),
                ('Fertilizers', 1.30)]
conn.executemany('INSERT INTO imports (commodity, value) VALUES (?, ?)', imports_data)

# Create a new table for trading partners
conn.execute('''CREATE TABLE IF NOT EXISTS trading_partners (
                country TEXT PRIMARY KEY,
                exports REAL,
                imports REAL
            )''')

# Insert data into trading partners table
trading_partners_data = [('United States', 15.87, 9.71),
                        ('United Arab Emirates', 11.62, 14.21),
                        ('China', 10.85, 78.44),
                        ('Hong Kong', 5.70, 1.72),
                        ('Singapore', 5.38, 3.20),
                        ('United Kingdom', 3.76, 2.66),
                        ('Netherlands', 3.53, 3.55),
                        ('Germany', 3.15, 8.20),
                        ('Bangladesh', 2.95, 0.81),
                        ('Vietnam', 2.71, 1.61)]
conn.executemany('INSERT INTO trading_partners (country, exports, imports) VALUES (?, ?, ?)', trading_partners_data)

# Commit changes to the database
conn.commit()

# Close the connection to the database
conn.close()