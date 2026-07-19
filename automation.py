import datetime
import os
import subprocess

import streamlit as st

os.chdir("/home/hashmi1997/committing-to-progress-automation")
# Set page styling
st.set_page_config(page_title="Progress Logger", page_icon="🚀", layout="centered")

st.title("🚀 Progress Sync Engine")
st.markdown("Log a daily session entry. Saving will update local storage and auto-push to GitHub.")
st.markdown("---")

# Form Inputs matching your taxonomy
st.subheader("📝 New Progress Entry")

domain = st.selectbox("Select Domain Focus", [
    "Advanced Math & Computing",
    "Full-Stack Web App Development",
    "Data Structures & Database Engineering",
    "Linux Workflows & Systems Architecture"
])

concept = st.text_input("Concept Synthesized", placeholder="e.g., Python f-string curly brace conflicts with LaTeX")
application = st.text_input("Practical Application Link / Scope", placeholder="e.g., Updated Section B in gui.py")
hurdle = st.text_area("Hurdle Encountered", placeholder="Describe the blockages or syntax traps faced...")
takeaway = st.text_area("Engineering Takeaway", placeholder="What structural rule or concept bypassed this issue?")

if st.button("💾 Commit & Push Progress", type="primary"):
    if not concept or not takeaway:
        st.error("Please fill out the core 'Concept' and 'Takeaway' fields before pushing.")
    else:
        # 1. Format the Entry using your README Markdown taxonomy
        today = datetime.date.today().strftime("%Y-%m-%d")

        markdown_entry = f"\n\n#### [🚀] Session: {today} — {domain}\n"
        markdown_entry += f"* 📝 **Concept Synthesized:** {concept}\n"
        markdown_entry += f"* 🛠️ **Practical Application:** {application if application else 'Local Environment Workspace'}\n"
        markdown_entry += f"* 🚧 **Hurdle Encountered:** {hurdle if hurdle else 'None. Smooth implementation.'}\n"
        markdown_entry += f"* 💡 **Engineering Takeaway:** {takeaway}\n"

        try:
            # 2. Append the entry to your tracking log file
            # Change "PROGRESS_LOG.md" to "README.md" if you want it directly on your main dashboard page
            target_file = "PROGRESS_LOG.md"

            with open(target_file, "a", encoding="utf-8") as file:
                file.write(markdown_entry)

            st.info("🔄 Local files updated. Initiating GitHub sync protocol...")

            # 3. Automate Git Actions using system shell parameters
            # Runs commands exactly like you do in your terminal
            commands = [
                ["git", "add", target_file],
                ["git", "commit", "-m", f"Logs: Automated progress sync for {today}"],
                ["git", "push"]
            ]

            for cmd in commands:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            st.success("🎉 Sync Complete! Progress committed and pushed safely to GitHub remote tree.")
            st.balloons()

        except subprocess.CalledProcessError as e:
            st.error(f"Git Automation Failure: {e.stderr}")
        except Exception as e:
            st.error(f"System Error: {str(e)}")
