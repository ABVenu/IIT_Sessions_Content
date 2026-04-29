# Pre-read: Time Series — When “When” Matters

Picture a kirana shop owner who notes down daily sales for a year. Or a farmer who tracks rainfall week by week. Or any of us watching the stock app and wondering whether the next number will go up or down. In all these cases, **the order of the numbers tells a story**. January does not come after December in the notebook for fun — **time is part of the meaning**. That idea is at the heart of this session.

Earlier in the course, you met machine learning where **shuffling rows was often fine** — each row was its own little world. Now we step into data where **yesterday genuinely speaks to today**. If someone handed you twelve months of electricity bills **in random order**, could you plan next summer’s AC usage? Could you honestly predict next Friday’s pizza orders if Fridays and Tuesdays were mixed up like cards in a deck? That is the puzzle: **many real decisions depend on sequences**, not on isolated snapshots.

This session introduces **time series** — data collected **in order over time**, where **past values influence what comes next**. We use the same spirit of “teaching the machine,” but we respect the calendar: **train on the past, check on the future**, use patterns like **long-run drift** and **repeating cycles**, and turn noisy daily jumps into **clear signals** the model can learn from. Tools such as **rolling windows** (think “average of the last few days”) and careful **evaluation** keep predictions honest instead of inflated.

One analogy from the notes sticks easily: **a rolling window is like updating your “last seven days” average every morning when you track walking or running.** You do not erase history — you slide the frame forward one day at a time and recompute “what happened lately?” That sliding frame is exactly how analysts speak of a **30-day moving average** on a chart: same logic, **different window size**, **same rule — only recent history inside the frame**.

In this pre-read, you'll discover:

- **Why** some datasets must stay in date order — and **why** mixing future rows into training misleads both you and the model.
- **How** to describe **trend** (the big direction over months or years) and **seasonality** (patterns that repeat on a schedule, like festivals or weekends).
- **What** **rolling windows** and **lag features** add when raw day-to-day numbers are too noisy on their own.
- **How** we **measure** forecasting errors fairly — including **MAPE**, which states mistakes as **percentages** so big numbers and small numbers can be compared sensibly.

A **time series** is simply **values lined up along time** — hourly, daily, monthly — **with the timestamp acting as anchor**. **Trend** answers “overall, are we climbing or sliding over the long haul?” — think smartphone adoption rising over a decade even if some months dip. **Seasonality** answers “does the same bump or dip **repeat on a clock**?” — ice cream in summer, orders spiking every Friday–Saturday, or sales lifting during festive weeks. Real series usually blend **both**: growth over years **plus** repeating yearly or weekly rhythms.

The beginner trap is treating time series like a normal spreadsheet and doing a **random train–test split**. That can accidentally put **tomorrow’s figures inside training**. The model then scores brilliantly on paper because it **peeked at the future** — something called **data leakage** here — but fails when deployed. The fix is a **chronological split**: **earlier periods train**, **later periods test**, as in real forecasting. Advanced courses go further with **walk-forward validation** (train on a growing past, test step by step forward); the live session will connect these ideas without drowning you in jargon.

**Rolling windows** smooth noise and **create new columns** — average, spread, max — over the last *N* steps so the model sees **recent behaviour**, not only a single spike. **Lag features** are simpler: **“What was yesterday’s value? What about the same weekday last week?”** — pulling the past into the same row as today. For **evaluation**, you still use ideas like **MAE** and **RMSE**, and you add **MAPE** when you want **“how far off in %”** instead of only rupees. You also compare against **baselines** — e.g. **“tomorrow equals today”** — because a fancy model must beat **obvious** rules.

By the end of the live class, you should be comfortable explaining **why order matters**, naming **trend vs seasonality**, **splitting data in time**, **building rolling and lag features**, and **interpreting MAPE** next to other errors — and you will know **when a metric is misleading** (for example, **MAPE** when actual values hit zero).

---

**What’s next — after this session you’ll be able to:**

- Describe real jobs and life situations where **time order** cannot be ignored.
- Sketch **why random splits break** forecasting and **what chronological splitting** achieves instead.
- Tell a friend the difference between **trend** and **seasonality** using an Indian example they relate to.
- Explain in one line what a **rolling window** does and why it helps a model.
- Read a **MAPE** number and say whether predictions are **roughly** in an acceptable band — and **when** to rely on **MAE** instead.

---

**Bring these to the live session — we’ll unpack the answers together:**

1. **If** you had March’s and July’s sales **swapped** in the training file but kept the dates wrong, **why** would your reported accuracy lie to you — and **what split rule** fixes that?

2. **Your shop shows higher sales every weekend and slow growth year on year.** **Which** part of that story is **trend**, **which** is **seasonality**, and **why** does a good model need **both** ideas?

3. **You build a 7-day rolling average of daily visitors.** **What** does the **first few rows** look like before the window is “full,” and **why** does that not mean your code is broken?

---

See you in class — bring your curiosity and one **real example** from your day (traffic, bills, steps, or sales). **Time** is on the syllabus this week.
