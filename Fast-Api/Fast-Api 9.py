import random
from fastapi import FastAPI
import uvicorn
app=FastAPI()
facts= [
"Some fish, like parrotfish, envelop themselves in a transparent mucus cocoon at night to protect themselves from predators.",
"Most fish do not have eyelids, so they never close their eyes, even when sleeping.",
"Fish can 'communicate' with each other using sounds; they produce clicks, thumps, or even purrs.",
"Sharks are the only fish that can blink with both eyes because they have a protective membrane.",
"The ocean sunfish (Mola mola) is the heaviest bony fish in the world, weighing over 2 tons.",
"Fish do not have external ears, but they hear perfectly well using their inner ear and a lateral line that detects vibrations in the water.",
"Some fish, such as electric eels, are capable of generating an electric shock of up to 600 volts.",
"Clownfish live in symbiosis with poisonous anemones, protected by a special layer of mucus that prevents them from being stung.",
"Deep-sea fish living where sunlight cannot reach often possess bioluminescence—the ability to glow in the dark.",
"Archerfish can knock down insects perched on branches above the water by accurately 'shooting' them with a jet of water from their mouths.",
]
@app.get("/")
def fact():
    try:
        return {"fact": random.choice(facts)}
    except Exception as error:
        return {"error": error}

if __name__ == "__main__":
    uvicorn.run(app)