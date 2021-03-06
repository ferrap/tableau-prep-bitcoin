# Tableau Prep flow including Python script to create a Bitcoin data source
The Prep flow [_Get Bitcoin Data.tflx_](https://github.com/ferrap/tableau-prep-bitcoin/blob/main/Get%20Bitcoin%20Data.tflx) allows to extract Bitcoin (BTC) historical data from the free API of [CryptoCompare](https://min-api.cryptocompare.com).

In the flow, there are additional steps to _historicise_ the data within the day when the Prep flow is run periodically throughout the day. This is useful if you want to increase the details in your data from daily (as retrieveved from the API) to the frequency determined by the execution of the flow.

![alt text](https://github.com/ferrap/tableau-prep-bitcoin/blob/main/Prep%20flow.jpg "Tableau Prep Flow")

Alternatively, I developed a [Web Data Connector](https://github.com/ferrap/tableau-wdc-bitcoin) to connect Tableau to Bitcoin data. Also, check [here](https://levelup.gitconnected.com/connect-tableau-to-bitcoin-data-a9ff1a03a4f4) for more information on this topic.
