import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

google = web.DataReader('GOOG', data_source = 'google', start = '3/14/2009', end = '4/14/2016')

# remove unused column
google = google.drop('Volume', axis = 1)

# add new column
google['Ticks'] = range(0, len(google.index.values))

# to pick  one-tenth(.1) by using random seed
one_tenth = google.sample(frac = .1, random_state = np.random.randint(10))
# one_tenth.index.name = None
one_tenth = one_tenth.sort_values(by=['Ticks'], ascending=[True])


# calucalte mid value
google['Rolling_Mean'] = google['Open'].rolling(window = 80).mean()

# if you want to reset index
google = google.reset_index()


def makeLinearPrediction():
    # filter : getting data only from tick 800 to 1200
    filt_google = google[(google['Ticks'] >= 800) & (google['Ticks'] <= 1200)]

    model = LinearRegression().fit(
        filt_google[['Ticks']], filt_google[['Rolling_Mean']]
    )

    m = model.coef_[0]
    b = model.intercept_
    print('y = ', round(m[0], 2), 'x + ', round(b[0], 2))

    predictions = model.predict(filt_google[['Ticks']])
    predictions = pd.DataFrame(data = predictions,
                               index = filt_google.index.values,
                               columns=['Pred'])
    # Join can concat , just like two table inner with tick column
    joined_df = filt_google.join(predictions, how = 'inner')

    fig = plt.figure()
    ax = fig.add_subplot(111);
    ax.plot(joined_df['Ticks'], joined_df['Rolling_Mean'], color=(0, 0, 0), linewidth=4,
            alpha= 0.2)
    ax.plot(joined_df['Ticks'], joined_df['Pred'], color=(1, 0, 0), label='Prediction')
    ax.set_title('Rolling Mean vs Linear Regression')

    # how match between prediction and real Rolling_Means
    import sklearn
    r_squared = sklearn.metrics.r2_score(joined_df['Rolling_Mean'], joined_df['Pred'], multioutput='uniform_average')
    r_squared

def showOrgInfoDiagram():
    # very simple plotting
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    axes[0].set_title('original plot')
    axes[0].set_xlabel('Ticks')
    axes[0].set_ylabel('Price')
    axes[0].plot('Ticks', 'Open', data=google)

    axes[1].set_title('Sampled Plot')
    axes[1].plot('Ticks', 'Open', data=one_tenth)

    axes[2].set_title('Smoothed (Rolling_Mean)')
    axes[2].plot('Ticks', 'Rolling_Mean', data=google)



showOrgInfoDiagram()

makeLinearPrediction()

plt.show()