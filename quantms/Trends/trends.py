def get_RSI_trend(RSI):
    print("->", RSI)
    if RSI >= 70:
        return "The current RSI value is over 70. According to J. Welles Wilder (1978), when a stock price gets over this value, it may be considered overbought, consider a possible reversion to a bearish trend"
    elif RSI <= 30:
        return "The current RSI value is under 30. According to J. Welles Wilder (1978), when a stock price gets under this value, it may be considered oversold, consider a possible reversion to a bullish trend"
    else:
        return "The RSI value is not currently above nor under any pre-determined key value"


def get_bollinger_trend(df):
    
    final_str = ''

    if df.iloc[-1]['Adj Close'] >= df.iloc[-1]['Sup_Band']:
        final_str += "For those who likes to short whenever an stock hits the superior band, this may be a adequate moment to buy puts or sell your stocks!\n"
    elif df.iloc[-1]['Adj Close'] <= df.iloc[-1]['Inf_Band']:
        final_str += "For those who likes to go long whenever an stock hits the inferior band, this may be a adequate moment to buy calls or buy stocks!\n"


    '''
        This for loop analyses the general trend of the stock in the last 30 days, the list's first index is the amount of days the stock has been closing
        above or below the moving average and try to suggest a trend.
        The second index means if its closing above (1) or below (-1) the mean, and it is supposed to change whenever it reverts its tendency
    '''
    isBullish = False
    cont_days = 0

    for i in range(30, 1, -1):
        if df.iloc[-i]['Adj Close'] >= df.iloc[-i]['RM']:
            if isBullish:
                cont_days += 1
            else:
                isBullish = True
                cont_days = 1
        else:
            if not isBullish:
                cont_days += 1
            else:
                isBullish = False
                cont_days = 1 

    if isBullish and cont_days >= 8:
        final_str += f'The Adjusted close price has been over the moving mean by {cont_days} days, this may be signalling an bullish trend!\n'
    elif isBullish == -1 and cont_days[0] >= 8:
        final_str += f'The Adjusted close price has been under the moving mean by {cont_days} days, this may be signalling an bearish trend!\n'
    else:
        final_str += "Our algorythm couldn't determine any reasonable trend in the last days!\n"
    
    return final_str