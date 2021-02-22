
#PropsAMC

URL: **http://127.0.0.1:8000/api/v1/get-geo-code/**
type: **POST**
Body: **CSV FILE Input **

Response: **OUT CSV File with lat lng**


**INPUT CSV FILE:**

| Address  |
| ------------ |
|   Kodampakkam, Chennai, Tamil Nadu,India  |
|  Sathyamangalam, Erode, India  |
|  Bangalore, India    |
| Delhi, India|


**OUTPUT CSV FILE:**

|Address   |  lat | lng  |
| ------------ | ------------ | ------------ |
|  Kodampakkam, Chennai, Tamil Nadu,India  | 39.78373 | -100.445882   |
|  Sathyamangalam, Erode, India |  11.658992 |  77.059611  |
|   Bangalore, India  | 12.97912  | 77.5913   |
| Delhi, India| 28.651718  | 77.221939   |
