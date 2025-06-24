print("Running Watsonx model classification...")

from credentials import WATSONX_API, WATSONX_PROJECT, WATSONX_URL, WATSONX_MODEL_ID
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

with open("pipeline_logs/clusters.txt") as f:
    logs = f.read()

prompt = f"""
Analyze the following clustered logs and determine the most likely root cause and a proposed solution:

{logs}

Respond in this format:
Root Cause: ...
Solution: ...
"""

model = ModelInference(
    model_id=WATSONX_MODEL_ID,
    credentials={"apikey": WATSONX_API, "url": WATSONX_URL},
    project_id=WATSONX_PROJECT
)

params = {
    GenParams.MAX_NEW_TOKENS: 200,
    GenParams.TEMPERATURE: 0.4,
    GenParams.DECODE_METHOD: "greedy"
}

response = model.generate_text(prompt=prompt, params=params)
print(response)