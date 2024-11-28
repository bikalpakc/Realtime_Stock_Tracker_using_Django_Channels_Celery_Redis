from celery import shared_task
import NepseData as nd
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

channel_layer=get_channel_layer() #gets and sets default channel layer described in settings.py file.

@shared_task(bind=True)
def update_stock(*args, **kwargs):
    selected_stock_list=["ADBL","CHDC","HLI","HRL","ILI","MANDU","NABIL","NRM","RNLI","RURU","SHEL","SJLIC","SNLI","SONA","SRLI"]
    selected_stock_data=[]
    for stock in selected_stock_list:
        stock_details=nd.get_data(stock)
        selected_stock_data.append({stock : stock_details})
    print(selected_stock_data)
    async_to_sync(channel_layer.group_send)('stocks', {'type':'send_stock_details', 'stock-details': json.dumps(selected_stock_data)}) #Send message to the Django Channels group and 'type' is the method that handles the send method. For e.g. if type is send_jokes, it is handled by method send_jokes in consumers.py file. whereas, 'text' is equivalent to 'context' in views.py of http request.
