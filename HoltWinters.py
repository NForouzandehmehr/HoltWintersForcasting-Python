from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
import rpy2.interactive as r
import datetime
from pytz import timezone




def HoltWinters(data, data_rang, prediction_range):
    base=importr('base')
    utils=importr("utils")
    utils.install_packages("forecast")
    c = robjects.r['c']
    res = robjects.IntVector(data)
    ts=  stat.ts(res,start=c(2015,6,27),frequency=7 )
    hw= stat.HoltWinters(ts)
    hwf= forecast.forecast_HoltWinters(hw, h=len(prediction_range))
    predicted=np.array(hwf.rx2('mean'))
    fitted= np.array(hwf.rx2('fitted'))
    return predicted



def Forcast(data, startDate, endDate):
    pacific= timezone('US/Pacific')
    today_date=(datetime.datetime.now(pacific)).date()
    end_date = datetime.date(year=int(endDate[0:4]), month=int(endDate[4:6]), day=int(endDate[6:8]))
    start_date = datetime.date(year=int(startDate[0:4]), month=int(startDate[4:6]), day=int(startDate[6:8]))
    tdf= len(data)
    data_range= np.linspace(1,tdf, tdf)
    td1= ((end_date - start_date).days+1)
    td2=int ((end_date - first_date).days)+1
    prediction_range= np.linspace(1,td2, td2)
    pred_data= HoltWinters(data, data_range, prediction_range)
    preds= (pred_data[-td1:]).tolist()                    
    roundedPreds = [ int(round(elem)) for elem in preds ]
    return roundedPreds

