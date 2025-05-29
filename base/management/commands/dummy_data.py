dev_bios = [
    "Full-stack dev with a passion for open source.",
    "Backend engineer specializing in Python and Django.",
    "Frontend enthusiast who loves React and Tailwind.",
    "DevOps engineer automating all the things.",
    "AI researcher exploring LLMs and NLP.",
    "Coding since 12, addicted to clean code.",
    "Always learning, mostly debugging.",
    "Building the web, one bug at a time.",
    "Full-stack engineer. Coffee enthusiast. Code is poetry.",
    "Pythonista with a love for clean syntax and bad puns.",
    "Turning caffeine into code since 2012.",
    "Building microservices and breaking monoliths.",
    "Frontend by day, backend by night. Pizza always.",
    "Rustacean trying not to fight the borrow checker.",
    "React dev with a soft spot for SolidJS.",
    "Django is my spirit animal 🦄.",
    "Still waiting for the perfect dark theme.",
    "Linux on the desktop. Fight me.",
    "Trying to get 100% test coverage and inner peace.",
    "I dream in TypeScript.",
    "🚀 Scaling apps and frying CPUs.",
    "DevOps by accident, YAML by choice.",
    "The answer is always `it depends`.",
    "Professional Googler. Stack Overflow top 3%.",
    "I write code that sometimes compiles.",
    "Functional programming changed my brain.",
    "C++ dev surviving in a garbage-collected world.",
    "Self-taught, battle-tested.",
    "On a mission to refactor the world.",
    "One commit away from greatness.",
    "Tabs over spaces. Yes, I said it.",
    "Async all the things!",
    "Learning Rust to forget JavaScript.",
    "Always breaking prod on Fridays.",
    "I do backend things with frontend feelings.",
    "Currently debugging why I chose this career.",
    "Certified merge conflict resolver.",
    "Hackathons are my happy place.",
    "Type safety is my love language.",
    "Building side projects I’ll never deploy.",
]

topic_names = [
    "JavaScript",
    "Python",
    "Rust",
    "Django",
    "C++",
    "Ruby on Rails",
    "SolidJS",
    "React",
]

host_messages = [
    # React
    "Optimize before you lag—let’s share perf tips!",
    "Redux? Zustand? Recoil? Let’s pick a side!",
    "Strong typing for your components? Let’s chat!",
    "Hooks changed everything. Let’s talk effects, refs, and gotchas!",
    # SolidJS
    "React devs welcome! Let’s compare mental models and performance.",
    "Let’s explore the philosophical difference between signals and state!",
    "Solid’s reactivity is 🔥. Ask anything about fine-grained updates.",
    # Ruby on Rails
    "Migrations, associations, and scopes—share your AR magic!",
    "Let’s appreciate how Rails makes the right choices for us.",
    # C++
    "Let’s talk low-latency C++ for real-time systems and games!",
    "Smart pointers, RAII—let’s write safer C++.",
    "C++ has come a long way. Share your favorite modern features!",
    # Django
    "Docker, Gunicorn, Nginx—share your smoothest deployment workflows.",
    "Signals and middleware: useful or overkill? Let’s debate!",
    "REST APIs with Django REST Framework—let’s build fast and right.",
    "Let’s dig into Django’s ORM—queries, relations, and performance tips!",
    # Rust
    "Generics, traits, performance—let's talk abstractions with no overhead!",
    "Welcome! Share your scars and triumphs against the borrow checker.",
    "Borrow checker? Ownership? You’re in the right place. Let’s chat!",
    # Python
    "Let's automate the boring stuff—share your best scripts!",
    "Explore the async side of Python—asyncio, aiohttp, and more!",
    "All things NumPy, pandas, and ML—let's dive in!",
    "Welcome! Let's talk idiomatic Python and elegant code.",
    # JavaScript
    "Ask anything about microtasks, call stack, and event queues. No more confusion!",
    "Map, reduce, pure functions—let’s get functional with JavaScript!",
    "Let’s talk raw JavaScript—no frameworks, just logic and the DOM!",
    "Welcome! Share your favorite modern JS tricks and ES features you can’t live without.",
    "Hey everyone! Let's unravel the async/await magic—bring your callback horror stories!",
]

participants_messages = [
    # React
    [
        "Memoization helped with my huge component trees.",
        "React Profiler helped me shave seconds off load times.",
    ],
    [
        "Zustand + hooks = simplicity.",
        "Recoil has the best mental model for me.",
    ],
    [
        "Types reduce bugs, but those errors can be cryptic!",
        "TSX is amazing for DX once you get used to it.",
    ],
    [
        "I feel you bro!",
        "I can’t live without custom hooks now.",
        "useEffect dependencies still confuse me.",
    ],
    [
        # SolidJS
        "Not yet :/",
        "What about SSR—anyone tried it in Solid?",
        "Solid’s JSX feels familiar but lighter.",
    ],
    [
        "Signals are so explicit, I actually understand what’s reactive.",
        "Solid’s execution model was a lightbulb moment for me.",
    ],
    [
        "Facts.",
        "Feels more like writing vanilla JS with superpowers.",
        "Signals > useState. Change my mind.",
    ],
    # Ruby on Rails
    [
        "has_many :through is so elegant.",
        "includes vs joins still confuses me at times.",
    ],
    [
        "Kinda works well for me.",
        "Anyone using Hotwire with Rails 7?",
        "I love how little setup Rails needs to get going.",
    ],
    # C++
    [
        "Threads + C++ = 🔥 (and sometimes 😵).",
        "I’ve used C++ for embedded systems. Timing is everything.",
    ],
    [
        "Unique pointers = fewer bugs for me.",
        "Shared ownership still confuses me sometimes.",
    ],
    [
        "Structured bindings in C++17 are a game-changer.",
        "auto everywhere! Saves so much time.",
    ],
    # Django
    [
        "Anyone using GitHub Actions for Django CI/CD?",
        "You said it, bro!",
        "WhiteNoise for static files = a lifesaver!",
    ],
    [
        "Middleware is great for request logging.",
        "I use signals for creating profile objects post-user creation.",
    ],
    [
        "Anyone using ViewSets with custom actions?",
        "Serializers are so powerful, yet confusing at times.",
    ],
    [
        "Any tips on handling complex filters?",
        "I love how select_related speeds things up.",
    ],
    # Rust
    [
        "impl Trait made my code so much cleaner!",
        "Man, programming can be tough!",
        "I still struggle with trait bounds sometimes.",
    ],
    [
        "Mutability rules are strict but keep things safe.",
        "You're right. It was tough reading through that part in the Rust Programming Language Book!",
        "Lifetimes made me cry at first, now I love them.",
    ],
    [
        "Enums + pattern matching = ❤️.",
        "Rust’s error handling feels clean once you get used to Result.",
    ],
    # Python
    [
        "My cron jobs now all run Python scripts. So handy.",
        "I love automating reports with openpyxl.",
    ],
    [
        "Took me a while to grok event loops in Python. Any tips?",
        "Running tasks concurrently with gather() was eye-opening.",
    ],
    [
        "I recently used scikit-learn for a side project—so intuitive!",
        "What’s your go-to way to clean missing data in pandas?",
    ],
    [
        "Anyone using dataclasses over regular classes?",
        "List comprehensions are so neat. Can’t go back!",
    ],
    # JavaScript
    [
        "Once I understood the event loop, my async code made sense.",
        "Still unclear what goes first—setTimeout or a promise?",
    ],
    [
        "Ramda and Lodash FP really helped me grok immutability.",
        "I find currying a bit abstract. Any good use cases?",
    ],
    [
        "Remember when jQuery was the only way? Times have changed!",
        "Manipulating the DOM manually is strangely satisfying.",
    ],
    [
        "Anyone using decorators in production yet?",
        "Optional chaining and nullish coalescing changed the game for me!",
    ],
    [
        "Have a look at the Udemy tutorial. I'll share the link later.",
        "Does anyone have a mental model for the event loop? It still trips me up.",
        "👍",
        "I used to chain .then() like a madman. Async/await saved my sanity.",
    ],
]
