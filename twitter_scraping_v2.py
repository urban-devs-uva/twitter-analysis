import asyncio
import csv
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    
    # Add accounts to the pool (use try-except to avoid duplicate account warnings)
    try:
        await api.pool.add_account("BillieC86559", "CSSciisthebest", "getscasselusa@gmail.com", "HopeThisWorks")
    except:
        pass  # Account already exists in the pool
    
    try:
        await api.pool.add_account("helga_de82706", "ThisBetterWork", "devrieshelga44@gmail.com", "ThisBetterWork")
    except:
        pass  # Account already exists in the pool
    
    await api.pool.login_all()

    keywords = ['buurthub', 'deelvervoer', 'deelauto', 'deelfiets', 'deelscooter', 'mobiliteitshub', 'wijkhub', 'stadshub', 'stadsrandhub', 'transferhub']
    date_range = 'since:2018-01-01 until:2023-11-30'

    tweets_data = []

    for keyword in keywords:
        q = f'{keyword} {date_range}'
        async for tweet in api.search(q, limit=1000):
            tweets_data.append((q, tweet.rawContent))


    csv_file_path = 'tweets_data5.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Keyword', 'Tweet Text'])
        csv_writer.writerows(tweets_data)

    print(f'Data saved to {csv_file_path}')

if __name__ == "__main__":
    asyncio.run(main())