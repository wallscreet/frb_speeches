from models import FederalReserve_RSS
import feedparser


frb = FederalReserve_RSS()

def main():
    # get list of urls from rss feed
    feed_url = frb.get_url_by_name("All Speeches and Testimony")

    # parse url to get feed
    feeds = feedparser.parse(feed_url)
    # print(feeds["entries"][0])

    # loop - fetch fed speech
    for entry in feeds["entries"]:
        speech_data = frb.fetch_fed_speech(url=entry.link)
        frb.append_speech_to_json(speech=speech_data)


if __name__ == "__main__":
    main()
