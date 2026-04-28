# Pre-read: Time Series — Understanding Data That Changes Over Time

Imagine you run a small medical store. Every morning before placing orders with your supplier, you look at the last few weeks of sales and ask yourself: "How much paracetamol do I need this week? Last week there was a spike — was it because of the fever season? Will it repeat?" You are not guessing randomly. You are reading patterns in time. You are, without knowing it, doing **time series analysis**.

This is exactly what massive companies do — Swiggy predicts order volumes by the hour, the Indian Railways forecasts passenger demand by the month, and hospitals plan medicine stock based on seasonal illness trends. All of them are reading data that is arranged in time order — and then making smart decisions from those patterns.

---

## When Order is Everything

Here is the challenge: most of what you have learned so far in machine learning assumes that each row in your dataset is independent. A student's marks row has nothing to do with the next student's row. You can shuffle the dataset and it does not matter.

But what happens when shuffling *destroys* the meaning?

Think about your bank account statement. What if someone shuffled the transactions randomly — credits and debits in a completely random order? The final balance would be wrong. The story of your spending would be gone. You could not tell if you were saving money or running out of it.

That is exactly the problem with time-based data. The *sequence* is the data. If you remove the order, you remove the intelligence.

Now ask yourself: how would you train a computer to predict next month's electricity demand for an entire city — when the correct answer depends not just on what happened last month, but also on what happened last year at the same time, and on the long-term trend of growing population and industry? Doing this by hand, for crores of data points, is impossible. You need a system — and that system starts with understanding time series.

---

## Meet the Hero: Time Series Analysis

**Time Series** is a way of working with data that is collected at regular intervals over time — hourly, daily, weekly, monthly. The key idea is that the *when* matters just as much as the *what*.

Think of it like a heartbeat monitor in a hospital. Every second, it records your heart rate. Each reading is connected to the one before it and the one after it. A doctor reading the monitor is not looking at individual numbers — they are reading the *shape* of the line over time. A sudden spike means something. A slow downward drift means something else. That shape, that pattern over time, is everything.

Time series analysis teaches the computer to read that shape — to separate what is a long-term direction from what is a repeating seasonal pattern, and to use that understanding to predict what comes next.

---

## The Two Biggest Patterns in Any Time Series

Before a computer can predict the future, it needs to understand two things happening in your data simultaneously.

The first is **Trend** — the big-picture direction. Are sales growing year over year? Is pollution getting worse decade by decade? Trend is like the slope of a long, gentle hill. There will be bumps along the way, but the general direction is clear.

The second is **Seasonality** — the repeating cycle. Every Diwali, online shopping spikes. Every Monday morning, coffee shop orders jump. Every summer, ice cream sales go up and woolen coat sales go down. Seasonality is predictable — it runs on a schedule.

Real data almost always has *both* happening at the same time. An e-commerce app might be growing every year (upward trend) AND spiking every October during the festive sale (seasonality). Pulling these two apart — understanding which part of the data is trend and which is seasonal — is one of the first things you do before building any model.

---

## Why You Cannot Use Your Old Toolkit Here

Here is something that will surprise most beginners: the train-test split you have been using until now will completely *break* when applied to time series data.

When you randomly split a time series dataset, you accidentally mix future data into your training set. Your model gets to "see the answer" during training. It will score very well on paper — but it will fail completely in the real world, because in real life you never have future data available when making a prediction. This problem has a name: **Data Leakage**.

The fix is simple but important: you always split time series data in *chronological order*. Old data trains the model. New data tests it. The model can only ever learn from the past.

---

## In This Pre-read, You'll Discover:

- How to identify **Trend** and **Seasonality** — the two hidden patterns in any time-based dataset
- Why the standard **random train-test split** is dangerous for time series and what to do instead
- How **Rolling Windows** let the model learn from recent history — like checking "what were my sales over the last 7 days?" instead of just yesterday
- How to measure whether your time series model is actually good using **MAE, RMSE, and MAPE** — three different ways to score a forecast

---

## What's Next — After This Session, You'll Be Able To:

- Look at any time-based dataset and immediately spot whether it has a trend, seasonality, or both
- Set up a correct, leak-free train-test pipeline for time series data
- Engineer powerful features using rolling windows and lag values
- Evaluate a forecasting model and know whether it is actually useful or just fooling you

---

## Curiosity Questions — Solved in the Live Session

These are real questions you might be wondering. We will answer all of them in the class:

1. **The flipped calendar puzzle:** If you accidentally train a time series model with a random split — and it scores 95% accuracy — how would you *prove* to your manager that the model is fake and will fail in production?

2. **The window size dilemma:** When building rolling window features, should you use the last 7 days or the last 30 days? What happens if you pick the wrong size — will the model overfit to noise, or miss important seasonal patterns altogether?

3. **The baseline trap:** Before building any complex model, data scientists always test a "naive forecast" — where the prediction for tomorrow is simply today's value. Can you think of a real business situation where this naive approach might actually be *better* than a sophisticated machine learning model?

Bring your thinking to the session — these questions will make a lot more sense once we get into the data together.
