import requests
import json
from pprint import pprint


r = requests.get("http://localhost/admin/api.php?summary")
#print r.json()
print ("Blocked today: %s" % r.json()["ads_blocked_today"])
print ("Queries today: %s" % r.json()["dns_queries_today"])
print ("Percent today: %s" % r.json()["ads_percentage_today"])
print ("Domains Holed: %s" % r.json()["domains_being_blocked"])




#write("Blocked today: %s" % r.json()["ads_blocked_today"])
#gotoLine2()
#write("Queries today: %s" % r.json()["dns_queries_today"])
#gotoLine3()
#write("%% blocked: %s" % r.json()["ads_percentage_today"])
#gotoLine4()
#write("Blocked: %s" % r.json()["domains_being_blocked"])

