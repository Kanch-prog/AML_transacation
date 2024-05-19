Detecting Anomalies in Financial Trnasactions for Anti-Money Laundring(AML)

Financial INstitutions face the ongoing challenege of detecting and preventing money fraud activities, and here is a proposal to analyze transaction data to identify anomalies that may indicate potential money laundering.

I have used transaction data obtained from https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml dataset available on Kaggle. It containes information including amounts and dates.

The dataset is prepocessed and performed EDA to see the distribution of transactio amounts and identify any potential trends and patterns.

Temporal trends in transaction amounts is analyzed to identify any irregularities over time, specificaly monthly basis and printing the monthly totals.

Histogram and line plot for visualization of distribution of trnasaction amounts and temporal trends.

Anomaly detection algorithm ( StandardScaler) is applied to detect outliers, by printing transactions with scaled amounts exceeding a predefined threshold.

![Capture3](https://github.com/Kanch-prog/AML_transacation/assets/121807277/fa27b3a9-134a-4044-b5e4-f73f5c4528ff)
![Capture2](https://github.com/Kanch-prog/AML_transacation/assets/121807277/82d9d26a-fa73-4ef2-aa7f-49dca33dd60d)
![Capture1](https://github.com/Kanch-prog/AML_transacation/assets/121807277/9eecf4e5-d69c-43a7-aed5-6a7fa39bf01c)
![Figure_2](https://github.com/Kanch-prog/AML_transacation/assets/121807277/da1fc8fe-2f62-4a00-b9e4-25115d630e01)

Observations:

More transactions fall into the low-value range.
There us an increasing trend in transaction amounts over time althought there is significant variability.
