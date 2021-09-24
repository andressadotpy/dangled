# dangled

## Installing 

`python3.8`

```bash
pip install -r requirements.txt
```

## How to use it

```python3
In [1]: from domain import Domain

In [2]: domain = Domain("andressa.dev")

In [3]: domain.monitor()
andressa.dev
A record:
['185.199.108.153']
AAAA record:
There's no data for this record type.
CNAME record:
[<DNS name andressadotpy.github.io.>]
MX record:
There's no data for this record type.
NS record:
There's no data for this record type.
TXT record:
There's no data for this record type.
```

**A dangling record is a vulnerability issue.** So for your domains that are in your DNS service and are expired/not being used anymore, the monitoring system will print out this message for each record:

```python3
A record:

                VULNERABILITY ISSUE:
                This domain doesn't exist anymore.
                Please delete all records pointing for this domain.
                
```


### Readings about DNS takeover and dangling DNS records

[1] - [All Your DNS Records Point to Us Understanding the Security
Threats of Dangling DNS Records](https://scholarworks.wm.edu/cgi/viewcontent.cgi?article=1829&context=aspubs)

[2] - [Dangling DNS: AWS EC2](https://infosecwriteups.com/dangling-dns-aws-ec2-e2d801701e8)