import pyautogui, time, random
import lmstudio as lms

model = lms.llm("llama-3.1-8b-lexi-uncensored-v2")

prompt_count = int(input("how many prompts? "))
prompts = []
for i in range(prompt_count):
    prompt = input(f"what nonsense to generate? {i + 1}: ")
    prompts.append(f"Write random facts about {prompt}. Can be made up. 5 facts each a sinle sentances of 5 - 10 words each. Do not write lists.")

count = int(input("count: "))
sentances = []

for i in range(count):
    print(f"- generating: {i+1}/{count}")
    request = random.choice(prompts)
    result = str(model.respond(request))
    for x in result.split("\n"):
        sentances.append(x)
        print(x)

input(f"{len(sentances)} are ready. [press enter to autospam]")
random.shuffle(sentances)
print("sleeping... 10s")
for i in range(10):
    print(i + 1)
    time.sleep(1)

for x in sentances:
    pyautogui.write(x, interval=random.random() / 2)
    pyautogui.press("enter")
    delay = random.random() + random.randint(2, 6)
    time.sleep(delay)