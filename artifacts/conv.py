import json

from cmflib import cmfquery

query = cmfquery.CmfQuery('/home/jaychaware2/cmf-server/data/mlmd')
json_payload = query.dumptojson(
                'Test-env',None
)
print(json.dumps(json.loads(json_payload),indent=4))
with open('test_mlmd_100_cmf.txt','w') as f:
    f.write(json.dumps(json.loads(json_payload),indent=4))
