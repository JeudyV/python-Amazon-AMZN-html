
import os
import json
import requests

def test():
    return {'hello': 'world'} 

def order_book():
    data = [
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        },
        {
            "AAPL": 'AAPL',
            "data1": "data1",
            "Price": "Price",
            "Data2": "Data2"
        }
    ]

    return data

def data_table():
     return {
      "data": [
        {
            "id": "1",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "2",
            "name": 'aaa',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "3",
            "name": 'ssss',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "4",
            "name": 'ddd',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "5",
            "name": 'fff',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "6",
            "name": 'ggg',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "7",
            "name": 'hhhh',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "8",
            "name": 'assas',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "9",
            "name": 'adsds',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "10",
            "name": 'dwdas',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "11",
            "name": 'ADfffccX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "12",
            "name": '12121',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "13",
            "name": 'dfcsd',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "14",
            "name": 'tfds',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "15",
            "name": 'vsdfwe',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "16",
            "name": 'sefse',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "17",
            "name": 'sefsefe',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "18",
            "name": 'sefsef',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "19",
            "name": 'AgtrergDX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "20",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "21",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "22",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "23",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "24",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "25",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "26",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "27",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "28",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "29",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "30",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "31",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "32",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "33",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "34",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "35",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "36",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "37",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "38",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "39",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "40",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
      ]
    }

def data_table2():
    return {
          "id": "1",
          "name": "Tiger Nixon",
          "stock": "System Architect",
          "status": "$320,800",
          "type": "2011/04/25",
          "Rating": "Edinburgh",
          "return": "5421",
          "annual_return": "5421",
          "risk_reward": "5421",
          "batting_AVG": "5421",
          "AVG": "5421"
        }
