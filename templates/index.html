<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduGenie — AI Learning Assistant</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

    <header class="masthead">
        <div class="masthead-inner">
            <p class="eyebrow">Study desk</p>
            <h1>EduGenie</h1>
            <p class="tagline">Your AI tutor for questions, explanations, quizzes, summaries, and study plans.</p>
        </div>
    </header>

    <main class="desk">

        <section class="notebook" id="qa">
            <div class="tab tab-blue">Ask</div>
            <div class="page">
                <h2>Ask a question</h2>
                <p class="hint">General knowledge, homework help, or anything you're stuck on.</p>
                <form id="qaForm" class="row">
                    <input type="text" id="question" placeholder="Why is the sky blue?" required>
                    <button type="submit">Get answer</button>
                </form>
                <div id="qaResult" class="output" data-empty="Your answer will appear here.">Your answer will appear here.</div>
            </div>
        </section>

        <section class="notebook" id="explain">
            <div class="tab tab-amber">Explain</div>
            <div class="page">
                <h2>Simplify a concept</h2>
                <p class="hint">A short, plain-language explanation of any topic.</p>
                <form id="explainForm" class="row">
                    <input type="text" id="topic" placeholder="Photosynthesis" required>
                    <button type="submit">Explain</button>
                </form>
                <div id="explanationResult" class="output" data-empty="Your explanation will appear here.">Your explanation will appear here.</div>
            </div>
        </section>

        <section class="notebook" id="summary">
            <div class="tab tab-green">Summarize</div>
            <div class="page">
                <h2>Summarize a passage</h2>
                <p class="hint">Paste a long paragraph or article to condense.</p>
                <form id="summaryForm" class="row">
                    <input type="text" id="summaryText" placeholder="Paste long content to summarize" required>
                    <button type="submit">Summarize</button>
                </form>
                <div id="summaryResult" class="output" data-empty="Your summary will appear here.">Your summary will appear here.</div>
            </div>
        </section>

        <section class="notebook" id="quiz">
            <div class="tab tab-rose">Quiz</div>
            <div class="page">
                <h2>Generate a quiz</h2>
                <p class="hint">Three multiple-choice questions from any topic or passage.</p>
                <form id="quizForm" class="row">
                    <input type="text" id="quizText" placeholder="Solar System" required>
                    <button type="submit">Generate quiz</button>
                </form>
                <div id="quizResult" class="output" data-empty="Your quiz will appear here.">Your quiz will appear here.</div>
            </div>
        </section>

        <section class="notebook" id="path">
            <div class="tab tab-blue">Plan</div>
            <div class="page">
                <h2>Get a learning path</h2>
                <p class="hint">A structured, beginner-to-advanced study plan with resources.</p>
                <form id="recommendForm" class="row">
                    <input type="text" id="recommendTopic" placeholder="SQL" required>
                    <button type="submit">Get plan</button>
                </form>
                <div id="recommendResult" class="output" data-empty="Your learning path will appear here.">Your learning path will appear here.</div>
            </div>
        </section>

    </main>

    <footer class="colophon">
        <p>EduGenie — built for the SmartBridge Google Cloud Gen AI Internship.</p>
    </footer>

    <script>
        function setLoading(el) {
            el.classList.remove("empty");
            el.innerText = "Working on it...";
        }

        function setResult(el, text) {
            el.classList.remove("empty");
            el.innerText = text;
        }

        // Q&A
        document.getElementById("qaForm").addEventListener("submit", async (e) => {
            e.preventDefault();
            const out = document.getElementById("qaResult");
            const question = document.getElementById("question").value;
            setLoading(out);
            const res = await fetch(`/qa?question=${encodeURIComponent(question)}`);
            const data = await res.json();
            setResult(out, data.answer);
        });

        // Explanation
        document.getElementById("explainForm").addEventListener("submit", async (e) => {
            e.preventDefault();
            const out = document.getElementById("explanationResult");
            const topic = document.getElementById("topic").value;
            setLoading(out);
            const res = await fetch("/explain/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ topic })
            });
            const data = await res.json();
            setResult(out, data.explanation || data.error);
        });

        // Summary
        document.getElementById("summaryForm").addEventListener("submit", async (e) => {
            e.preventDefault();
            const out = document.getElementById("summaryResult");
            const text = document.getElementById("summaryText").value;
            setLoading(out);
            const res = await fetch("/summarize/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text })
            });
            const data = await res.json();
            setResult(out, data.summary || data.error);
        });

        // Quiz
        document.getElementById("quizForm").addEventListener("submit", async (e) => {
            e.preventDefault();
            const quizDiv = document.getElementById("quizResult");
            const text = document.getElementById("quizText").value;
            setLoading(quizDiv);
            const res = await fetch("/quiz", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text })
            });
            const data = await res.json();
            quizDiv.classList.remove("empty");
            quizDiv.innerHTML = "";

            if (data.quiz && !data.quiz.error) {
                data.quiz.forEach((q, i) => {
                    const qBlock = document.createElement("div");
                    qBlock.className = "quiz-question";
                    qBlock.innerHTML = `
                        <p class="q-title">Question ${i + 1}<span>${q.question}</span></p>
                        <div class="q-options">
                            ${q.options.map((opt, j) => `
                                <label>
                                    <input type="radio" name="q${i}" value="${opt}">
                                    <span>${opt}</span>
                                </label>
                            `).join("")}
                        </div>
                        <button type="button" data-index="${i}" class="checkAnswerBtn">Check answer</button>
                        <p class="answerFeedback" id="feedback${i}"></p>
                    `;
                    quizDiv.appendChild(qBlock);
                });

                document.querySelectorAll(".checkAnswerBtn").forEach(btn => {
                    btn.addEventListener("click", () => {
                        const i = btn.getAttribute("data-index");
                        const selected = document.querySelector(`input[name="q${i}"]:checked`);
                        const feedback = document.getElementById(`feedback${i}`);
                        if (!selected) {
                            feedback.className = "answerFeedback neutral";
                            feedback.innerText = "Select an option first.";
                            return;
                        }
                        if (selected.value === data.quiz[i].answer) {
                            feedback.className = "answerFeedback correct";
                            feedback.innerText = "Correct.";
                        } else {
                            feedback.className = "answerFeedback incorrect";
                            feedback.innerText = `Incorrect. Correct answer: ${data.quiz[i].answer}`;
                        }
                    });
                });
            } else {
                setResult(quizDiv, "Could not generate a quiz. Try again.");
            }
        });

        // Learning Recommendations
        document.getElementById("recommendForm").addEventListener("submit", async (e) => {
            e.preventDefault();
            const out = document.getElementById("recommendResult");
            const topic = document.getElementById("recommendTopic").value;
            setLoading(out);
            const res = await fetch(`/learn/recommendations?topic=${encodeURIComponent(topic)}`);
            const data = await res.json();
            setResult(out, data.recommendation);
        });
    </script>
</body>
</html>
