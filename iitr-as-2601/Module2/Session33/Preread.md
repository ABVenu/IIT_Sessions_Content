# Pre-read: Time Series — Understanding Data That Changes Over Time

## When the "When" Is as Important as the "What"

Picture this: you are the demand planner for a large supermarket chain. Every week, you must decide how much stock to order — vegetables, beverages, snacks, everything. Order too little, and shelves go empty on the weekend rush. Order too much, and perishables rot in the warehouse.

Now here is the challenge. Every month, sales are different. Every festive season, demand spikes dramatically. Every Monday morning after a long weekend, footfall drops. The data is changing constantly, and the changes follow patterns — patterns tied to *when* something happens, not just *what* happened.

How do you predict something like that?

---

## The Problem With "Normal" Data Thinking

So far in your learning journey, you have worked with datasets where each row is its own story. A list of houses with their prices. A collection of customer records. In those datasets, row number 50 has nothing to do with row number 49. You could shuffle the entire spreadsheet, and your model would still work perfectly.

But what if that is not true for your data?

Imagine someone hands you a spreadsheet of daily rainfall readings for the past five years. If you randomly shuffled those rows, would the data still make sense? Absolutely not — because March's rainfall coming right after October's reading tells your model a nonsensical story. The *order* of data is the entire point.

This is exactly the problem that trips up beginners when they first encounter real-world forecasting data. They try the same techniques that worked before — random splits, standard accuracy checks — and the results are terrible. Not because the model is bad, but because the *approach* was wrong from the start.

---

## Enter Time Series — A Completely Different Way of Thinking About Data

A **Time Series** is simply a list of numbers recorded in time order — daily, weekly, monthly — where the *sequence itself carries meaning*. Think of it like a patient's health chart in a hospital. The readings are recorded every hour. The doctor does not just look at the latest reading in isolation — they look at how it has changed over time. Rising? Falling? Stable? The pattern over time is the diagnosis.

In this session, you will learn the tools and thinking required to handle exactly this kind of data. And it shows up *everywhere*:

- Predicting how many rides an app will get next Friday
- Forecasting electricity demand for the next week
- Estimating how much stock a medicine company needs for the flu season
- Anticipating website traffic before a product launch

---

## The "DNA" of Every Time Series

Before you can model or predict anything, you need to understand what is hidden inside time series data. Every time series has two fundamental patterns embedded in it — think of them as its DNA.

The first is **Trend** — the long-term direction the data is heading. Is it generally going up over months and years? Or coming down? Think of the number of people using smartphones in India between 2010 and 2024. Every year, more people joined. There were dips and flat months, but the *overall direction* was clearly upward. That is a trend.

The second is **Seasonality** — repeating patterns that occur on a schedule. Ice cream sales in any Indian city will peak every April–June and dip every November–January, year after year. Pizza delivery apps see their biggest spike every Friday night. These patterns are not random — they are predictable and cyclical. Once you learn to spot them, your forecasts immediately become much more reliable.

Most real-world data has *both* — a long-term trend and a repeating seasonal pattern layered on top of each other. Spotting and separating these two is your first superpower in time series analysis.

---

## In this pre-read, you'll discover:

- Why time series data is fundamentally different from the datasets you have worked with before — and why that changes *everything* about how you handle it
- What **Trend** and **Seasonality** mean, and how to recognise them in any dataset
- Why splitting your data randomly is one of the worst mistakes you can make in time series work — and what the right approach looks like
- How **Rolling Windows** turn raw historical data into powerful features that give your model a "memory" of recent patterns

---

## One Powerful Analogy to Carry With You

Think of a Rolling Window like this: imagine you are a cricket commentator tracking a batsman's recent form. You do not care about his entire career average — you want to know how he has performed in the *last 5 matches*. Every match, you drop the oldest game from your calculation and add the newest one. Your "window" of 5 matches *rolls forward* with each new game.

This is exactly what a Rolling Window does with time series data. Instead of looking at every historical data point equally, it focuses on the most recent window of N days — computing averages, ranges, or other statistics — and slides forward one step at a time. It gives your model a realistic, recency-weighted view of what is happening, rather than treating data from three years ago as equally important as last week.

---

## How Will You Know If Your Model Is Any Good?

One more thing you will explore in this session is *evaluation* — how to measure whether your time series model is actually performing well or just looking good on paper.

You already know about MAE and RMSE from earlier sessions. In time series work, a third metric becomes very important: **MAPE** (Mean Absolute Percentage Error). Instead of saying "my prediction was off by ₹200," MAPE says "my prediction was off by 8%." This percentage-based view makes it easy to compare performance across products with completely different price ranges — you cannot fairly compare a ₹200 error on a ₹500 product with a ₹200 error on a ₹50,000 product, but an 8% error is an 8% error either way.

You will also learn about **Baseline Models** — the simplest possible prediction strategies that any decent model must beat. If your sophisticated model cannot outperform "just predict tomorrow will be the same as today," something has gone seriously wrong.

---

## Questions to Sit With Before the Session

Come to the live class ready to think about these:

1. A mobile app tracks the number of daily active users over two years. You notice that every December the numbers drop sharply, and every January they spike back up. Is this a Trend, Seasonality, or both — and why does the answer matter for your forecast?

2. A student builds a time series model to predict stock prices. They randomly split their data — 80% for training and 20% for testing. The model scores very well on the test set. But when deployed, it performs terribly. What went wrong, and how would you fix it?

3. You are computing a 7-day rolling average of sales. On Day 1 and Day 2 of your dataset, the rolling average shows a blank (NaN). Why does this happen, and is it a problem or expected behavior?

---

## After This Session, You Will Be Able To

- Identify time series data in the wild and explain why it must be handled differently
- Describe Trend and Seasonality to anyone, using real-life examples
- Correctly split time series data without causing data leakage
- Build rolling window features in Python that give your model a "memory" of recent history
- Calculate and interpret MAPE alongside MAE and RMSE to evaluate forecast quality
- Establish a baseline model and use it as the minimum bar your model must clear
