from flask import Flask, render_template_string

app = Flask(__name__)

DOWNLOAD_LINK = "https://drive.google.com/uc?export=download&id=1izg3R8JD3kKGALDU0lmlIXXdkbd92o1K"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>STAR SYSTEM — Free macOS App</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body {
            background:
                radial-gradient(
                    circle at 50% 20%,
                    #12304a 0%,
                    #050914 45%,
                    #020308 100%
                );
        }

        .glow {
            box-shadow:
                0 0 25px rgba(34, 211, 238, 0.3),
                0 0 70px rgba(34, 211, 238, 0.1);
        }
    </style>
</head>

<body class="min-h-screen flex items-center justify-center text-white">

    <main class="text-center px-6">

        <div class="text-cyan-400 font-semibold mb-4">
            ✦ FREE macOS APPLICATION
        </div>

        <h1 class="text-6xl md:text-8xl font-black mb-6">
            STAR <span class="text-cyan-400">SYSTEM</span>
        </h1>

        <p class="text-xl text-slate-300 mb-3">
            Your futuristic desktop workstation.
        </p>

        <p class="text-slate-400 max-w-xl mx-auto mb-10">
            Useful tools packed into one sleek cyber-themed macOS application.
        </p>

        <a
            href="{{ download_link }}"
            class="inline-block glow bg-cyan-500 hover:bg-cyan-400
                   text-black font-bold text-lg px-10 py-5
                   rounded-full transition hover:scale-105"
        >
            🚀 DOWNLOAD STAR SYSTEM
        </a>

        <p class="text-sm text-slate-500 mt-5">
            Free • macOS • No subscription
        </p>

        <div class="mt-12 text-slate-400">
            QR Generator • Calculator • Stopwatch • Time Tools • More
        </div>

    </main>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        download_link=DOWNLOAD_LINK
    )

if __name__ == "__main__":
    app.run(debug=True)
