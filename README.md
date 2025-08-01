# Federal Reserve Board RSS
**Members Speeches and Testimony Parser**

A lightweight Python pipeline to ingest, deduplicate, scrape, and summarize speeches, testimony, and comments published by Federal Reserve Board members. The resulting structured and summarized content is intended for use as model context, monitoring, analysis, or downstream NLP workflows—built to stay lean on cost by leveraging Grok-3-mini via the XAI API.

---

## Goals / Intent

- Continuously pull new public statements (speeches, testimony, comments) from the Federal Reserve Board RSS feed.  
- Scrape the full content and metadata from each linked page.  
- Deduplicate by speaker + URL so API calls are only spent on novel content.  
- Generate concise summaries with Grok-3-mini (XAI API) for downstream consumption (research dashboards, alerting, embedding context, etc.).  
- Persist raw and structured outputs for auditability and further modeling.

---

## Features

- **RSS ingestion** via `feedparser` from the Federal Reserve Board’s public feeds.  
- **HTML scraping** with BeautifulSoup to extract the full textual content and relevant metadata (speaker, title/date, URL, etc.).  
- **Deduplication** using the combination of speaker identity and source URL to avoid reprocessing the same item.  
- **Summarization** of each speech/testimony using Grok-3-mini (XAI API) to produce human-readable concise abstracts.  
- **Pydantic models** (suggested) to validate and structure the scraped + summarized data.  
- **JSON persistence** for raw and processed records.

---

## Setup (with Astral UV)

1. **Install UV** (if not already present):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

Or via pipx:

```bash
pipx install uv
```

2. **Initialize and add dependencies**

```bash
uv init
uv add openai bs4 feedparser pydantic
uv sync
```

This creates and locks the virtual environment in `uv.lock` and makes execution reproducible.

3. **Set your environment variables**

```bash
export XAI_API_KEY="your_xai_api_key_here"  # for Grok-3-mini via XAI
```

(Adjust the variable name if your client wrapper expects something different.)

4. **Run the pipeline**

```bash
uv run python main.py
```

---

## Output Example (simplified JSON)

```json
{
  "speaker": "Governor Christopher J. Waller",
  "speeches": [
    {
      "title": "Statement by Governor Christopher J. Waller",
      "date": "2025-08-01T00:00:00",
      "location": "",
      "url": "https://www.federalreserve.gov/newsevents/speech/waller20250801a.htm",
      "summary": "Below is a concise summary of the speech/testimony by Federal Reserve Board Governor Christopher J. Waller, based on the provided text:\n\n### Summary of Christopher J. Waller's Speech/Testimony\n\nIn his remarks, Governor Waller explained his dissent at the recent Federal Open Market Committee (FOMC) meeting, where he advocated for a 25 basis points cut in the policy rate, consistent with views he expressed in a July 17 speech. He outlined three primary reasons for his position:\n\n1. **Tariffs and Inflation**: Tariffs represent temporary price increases that do not sustain inflation, and standard central banking practice is to \"look through\" these effects when inflation expectations remain anchored, as they currently are.\n\n2. **Monetary Policy Stance**: Economic data indicates that policy is overly restrictive. Real GDP growth was 1.2% in the first half of the year and is expected to stay soft, while the unemployment rate (4.1%) is near its long-run estimate. Inflation is slightly above the 2% target, excluding temporary tariff effects, suggesting the policy rate should be near the neutral level (estimated at 3%), rather than 1.25-1.50 percentage points above it.\n\n3. **Labor Market Risks**: While the labor market appears stable on the surface, data revisions show private-sector payroll growth nearing stall speed, with increased downside risks. Given that underlying inflation is near target and upside inflation risks are limited, Waller argued against delaying rate cuts until the labor market deteriorates.\n\nWaller respected his colleagues' \"wait and see\" approach to tariffs' potential inflationary effects, viewing such differences as part of a healthy policy debate. However, he criticized this strategy as overly cautious, warning that it could lead to policy lagging behind economic realities. He noted that tariff impacts have been minimal so far and that waiting might risk a rapid labor market downturn. Instead, he proposed an immediate rate cut to allow for data-driven adjustments: if inflation surprises upward, the FOMC could pause; if not, further gradual reductions could proceed. Overall, Waller emphasized the need to act proactively to avoid unnecessarily endangering the labor market.",
      "content": "At the most recent Federal Open Market Committee (FOMC) meeting, I dissented because I concluded that cutting the policy rate by 25 basis points was the appropriate stance of policy. In a speech I gave July 17, I laid out the case for cutting the policy rate at the July FOMC meeting and my views have not changed since then. I will recap the reasons for doing so.\nFirst, tariffs are one-off increases in the price level and do not cause inflation beyond a temporary increase. Standard central banking practice is to \"look through\" such price-level effects as long as inflation expectations are anchored, which they are.\nSecond, a host of data argues that monetary policy should now be close to neutral, not restrictive. Real gross domestic product (GDP) growth was 1.2 percent in the first half of this year and is expected to remain soft for the rest of 2025, much lower than the median of FOMC participants' estimates of longer-run GDP growth. Meanwhile, the unemployment rate is 4.1 percent, near the Committee's longer-run estimate, and total inflation is close to our target at just slightly above 2 percent if we put aside tariff effects that I believe will be temporary. Taken together, the data imply the policy rate should be around neutral, which the median FOMC participant estimates is 3 percent, and not where we areâ1.25 to 1.50 percentage points above 3 percent.\nMy final reason to favor a cut now is that while the labor market looks fine on the surface, once we account for expected data revisions, private-sector payroll growth is near stall speed, and other data suggest that the downside risks to the labor market have increased. With underlying inflation near target and the upside risks to inflation limited, we should not wait until the labor market deteriorates before we cut the policy rate.\nI fully respect the views of my colleagues on the FOMC that suggest we need to take a \"wait and see\" approach regarding tariffs' effects on inflation. There is nothing wrong about having different views about how to interpret incoming data and using different economic arguments to predict how tariffs will impact the economy. These differences are a sign of a healthy and robust policy discussion.\nBut, I believe that the wait and see approach is overly cautious, and, in my opinion, does not properly balance the risks to the outlook and could lead to policy falling behind the curve. The price effects from tariffs have been small so far, and since we will likely not get clarity on tariff levels or their ultimate impact on the economy over the course of the next several months, it is possible that the labor market falters before that clarity is obtainedâif it ever is obtained. When labor markets turn, they often turn fast. If we find ourselves needing to support the economy, waiting may unduly delay moving toward appropriate policy.\nMy position does not mean I believe the FOMC should reduce the policy rate along a predetermined path. We can cut now and see how the data evolves. If the tariff effects do not lead to a major shock to inflation, the Committee can continue reducing the rate at a moderate pace. If we do get significant upside surprises to inflation and employment, we can pause. But I see no reason that we should hold the policy rate at its current level and risk a sudden decline in the labor market."
    },
  ]
}
```

