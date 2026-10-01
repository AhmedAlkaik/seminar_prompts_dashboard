import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="Prompt Control Tower",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for Theme, Typography, and Styling
# - Background: Soft off-white (#F8F9FA)
# - Text: Dark Slate (#2B2D42)
# - Accents/Headers: Muted Navy Blue (#3D5A80)
# - Cards: Pure White (#FFFFFF) with shadow
# - Font: sans-serif base size 16px
custom_css = """
<style>
    /* Global Font and Text Color */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Roboto', 'Segoe UI', sans-serif;
        font-size: 16px;
        color: #2B2D42 !important;
    }

    /* Main background color */
    .stApp {
        background-color: #F8F9FA;
    }

    /* Headers / Accents */
    h1, h2, h3, h4, h5, h6 {
        color: #3D5A80 !important;
        font-family: 'Inter', 'Roboto', 'Segoe UI', sans-serif;
    }

    /* Override standard Markdown text color */
    p {
        color: #2B2D42 !important;
    }

    /* Expander (Card) Customization */
    .streamlit-expanderHeader {
        background-color: #FFFFFF !important;
        color: #3D5A80 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        border-radius: 8px 8px 0 0 !important;
        border: none !important;
    }
    
    [data-testid="stExpander"] {
        background-color: #FFFFFF;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.025);
        border: 1px solid #E2E8F0;
        margin-bottom: 1.5rem;
    }

    /* Remove default top border on expander details for a seamless card look */
    [data-testid="stExpanderDetails"] {
        border-top: 1px solid #E2E8F0;
        padding: 1.5rem !important;
    }

    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }

    /* Engineering Verdict Box Styling */
    .verdict-box {
        background-color: #E6F0FA; /* Soft muted blue */
        border-left: 5px solid #3D5A80;
        padding: 15px;
        border-radius: 0 4px 4px 0;
        margin-top: 15px;
        color: #2B2D42;
        font-size: 15px;
        line-height: 1.5;
    }
    
    /* Academic Disclaimer Box in Sidebar */
    .disclaimer-box {
        font-size: 13px;
        color: #4A5568;
        background-color: #F8F9FA;
        border: 1px solid #E2E8F0;
        padding: 15px;
        border-radius: 6px;
        margin-bottom: 25px;
        line-height: 1.4;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# ==========================================
# 2. MOCK DATA (The "Evidence" Format)
# ==========================================
prompt_data = [
    {
        "phase": "Phase 1: Presentation Ideation",
        "title": "Master Theme & Introduction Slides",
        "objective": "Design a highly professional, visually sophisticated master template and introductory slides that establish a premium aerospace/industrial engineering aesthetic.",
        "raw_prompt": """ROLE & OBJECTIVE Act as a senior presentation designer for a top-tier aerospace/industrial engineering firm. Design a highly professional, visually sophisticated master template and the first two introductory slides for a 15- minute university engineering seminar titled "NON-CONVENTIONAL MACHINING".

GLOBAL THEME & LIGHT AESTHETIC
Background: Use a premium light palette (e.g., stark white #FFFFFF to light cool- gray #F5F7F8).
Typography: Use a modern geometric sans-serif (like Helvetica Now, Roboto, or Inter). Use deep charcoal or almost-black (#1A1A1A) for text to ensure high contrast.
Visual Style: Minimalist, precise, breathable, and scientific. It should look like an MIT R&D whitepaper or a premium engineering consultancy deck.
Grid & Layout: Use a strict, asymmetrical editorial grid. Utilize generous whitespace and precise, thin-line borders or crosshairs for technical flavor. Avoid centering everything.
Color Accents: Use colors sparingly and only for technical emphasis.
• Electric cyan (Electrical)
• Amber/Orange (Thermal)
• Subtle teal (Electrochemical)
• Muted blue (Fluid/Abrasive)
Avoid: Generic blue PowerPoint templates, drop-shadows, clip-art, 3D text, glowing neon effects, or large blocks of text.

GLOBAL FOOTER SYSTEM (MUST BE ON EVERY SLIDE)
Bottom Left: "NON-CONVENTIONAL MACHINING" in small, tracked-out, uppercase text.
Bottom Right: Slide numbering in a "01 / 15" format.

SLIDE 01: THE CHALLENGE (TITLE SLIDE)
Layout: Split the slide. One side features a large, dramatic, high-resolution macro photograph of an extremely complex, precision-engineered metal component...

SLIDE 02: THE PHYSICAL LIMIT
Layout: Minimalist and asymmetric. Use a high-quality macro image showing a conventional cutting tool (like a milling cutter) that is worn, broken, or physically too large...""",
        "engineering_verdict": "<strong>ACCEPTED WITH MODIFICATIONS.</strong> The AI provided an excellent structural foundation for the editorial grid. We adopted the color coding (Cyan for Electrical, Amber for Thermal) but manually sourced the macro photography to ensure they depicted accurate 5-axis milled superalloys rather than generic AI-generated metal."
    },
    {
        "phase": "Phase 1: Presentation Ideation",
        "title": "Thermal Machining Concept Structuring",
        "objective": "Organize the technical explanation of thermal machining for a strict 3-minute delivery, ensuring complex mechanisms are explained simply.",
        "raw_prompt": """I am preparing the Thermal Machining section of a Non-Conventional Machining seminar. Based on the topics and questions I have been discussing with you, help me organize and explain the content I actually need:

• A short definition of thermal machining and its working principle.
• Explain Laser Beam Machining, Electron Beam Machining, and Plasma Arc Machining, focusing on how each works and removes material.
• Answer my technical questions: why the whole workpiece does not melt or evaporate, how to minimize microstructural changes, and how the laser beam passes through the nozzle without melting it, including the role of the lens, focal point, and assist gas, and I want you to tell me the most popular questions that people ask you on this part with their answers

Keep the explanation clear and technically accurate, starting from the basics. Use concise English for slide content and detailed, simple explanations in Egyptian Arabic for speaking and answering questions to be like you are explaining to people who do not know anything in engineering.

And the data that I want for the presentation I don’t want exceeds 3 minutes.""",
        "engineering_verdict": "<strong>ACCEPTED.</strong> The AI successfully structured the complex physics (lens, focal point, assist gas) into a 3-minute bilingual framework. We verified the answers regarding microstructural changes (HAZ) against Kalpakjian & Schmid before including them in the final script."
    },
    {
        "phase": "Phase 1: Presentation Ideation",
        "title": "Mechanical Machining Slide Generation",
        "objective": "Generate a minimalist, keyword-based slide sequence for Mechanical Non-Conventional Machining (USM, AJM, WJM, AWJM).",
        "raw_prompt": """Create slides for a seminar presentation titled "Mechanical Non-Conventional Machining".

Style: minimal, keyword-based slides, consistent header ("2. Mechanical machining") on every slide.

Structure:
1. Introduction: the question "What is mechanical non-conventional machining?" with a hook question "What is the difference between it and traditional machining?"
2. Types overview: list all four types, USM, AJM, WJM, AWJM (names + abbreviations).
3. Ultrasonic Machining (USM): how it works. Short flow (vibrating tool → abrasive slurry → material erosion), best for hard and brittle materials.
4. Abrasive Jet Machining (AJM): compressed air + abrasives → etching and engraving surfaces, and list it's common disadvantages.
5. Water Jet Machining (WJM): high-pressure water stream → cutting/drilling of stone and soft metals.
6. Abrasive Water Jet Machining (AWJM): WJM + abrasives → cuts harder materials
7. When to use it: heat-sensitive

use the same font and theme across the whole ppt + add schematic diagram for each type of machining to the right of the text.""",
        "engineering_verdict": "<strong>MODIFIED.</strong> The AI generated the correct flow, but we manually curated the schematic diagrams from verified engineering textbooks rather than relying on AI-generated images to guarantee technical accuracy of the tool/workpiece interface."
    },
    {
        "phase": "Phase 1: Presentation Ideation",
        "title": "Electrical Discharge Machining Storyboard",
        "objective": "Create a 9-slide storyboard for EDM that maintains the premium visual aesthetic while explaining the progression from limitation to application.",
        "raw_prompt": """Create a professional 9-slide university engineering presentation about ELECTRICAL DISCHARGE MACHINING (EDM).

Use the attached presentation as the EXACT visual reference. Make the new slides look like they belong to the SAME presentation—same typography, layout, colors, spacing, labels, and visual style. Do not use a generic template.

STYLE: Minimal industrial/aerospace aesthetic, light background, bold black uppercase typography, large realistic engineering images, generous whitespace, thin technical elements, very little text. No gradients, icons, cartoons, or corporate stock imagery.

SLIDES:
“WHEN MECHANICAL CUTTING REACHES ITS LIMIT.” — complex geometry/cavity.
“ONE SPARK. ONE MICRO-CRATER.” — electrode, spark, workpiece, crater.
“ELECTRICAL DISCHARGE MACHINING” — EDM machine + one-line definition.
“HOW EDM REMOVES MATERIAL” — gap → dielectric → breakdown → spark → melting → flushing.
“THE SPARK HAS SETTINGS.” — Voltage, Current, Pulse On/Off Time, Gap.
“WHAT IF THE ELECTRODE WAS A WIRE?” — introduce Wire EDM.
“WIRE EDM” — machine + minimal technical labels.
“THE ADVANTAGES / THE LIMITATIONS” — balanced comparison.
“FROM SPARK TO COMPONENT.” — gas tube valve die application from the reference.

Keep the story:
LIMIT → SPARK → EDM → PARAMETERS → WIRE EDM → ADVANTAGES/LIMITATIONS → APPLICATION.

Use technically accurate visuals and extremely concise text. Every slide should have ONE strong visual idea. Do not display slide numbers.""",
        "engineering_verdict": "<strong>ACCEPTED.</strong> This prompt successfully forced the AI to adhere to our strict narrative flow (Limitation -> Mechanism -> Parameters -> Application). The resulting text was minimalist enough to prevent the audience from reading ahead of the speaker."
    },
    {
        "phase": "Phase 2: LaTeX Architecture & Report Formatting",
        "title": "Foundational LaTeX Architecture",
        "objective": "Develop the foundational LaTeX architecture for a 12-page academic report perfectly mirroring the presentation flow.",
        "raw_prompt": """Act as a Senior Industrial and Manufacturing Engineering Researcher.

Task: Develop the foundational LaTeX architecture for a 12-page academic report based on the attached presentation.

Objectives & Constraints:

Synchronization: The report's structure must perfectly mirror the flow and core arguments of the attached presentation.

Modular Architecture: Output clean, fully compilable LaTeX code with explicitly commented placeholder sections, enabling multiple team members to seamlessly insert their respective contributions.

Academic Rigor: Include a formal cover page, consistent typography settings, and placeholder structures for real, verifiable academic citations.

Evaluation Criteria: Focus heavily on granular engineering report standards. The output will be evaluated on formatting precision, structural logic, and adherence to professional academic documentation practices.""",
        "engineering_verdict": "<strong>ACCEPTED.</strong> The AI generated a robust, fully compilable modular LaTeX structure. The engineering team verified the preamble packages and utilized the placeholder commenting system to divide the workload without encountering synthesis configuration conflicts."
    },
    {
        "phase": "Phase 3: Content Refinement",
        "title": "Master Workflow Template Generation",
        "objective": "Establish a consistent prompt template for all future seminar modules to guarantee uniformity in reports, scripts, and slide formatting.",
        "raw_prompt": """Here is a single, consolidated prompt combining all your instructions into one template you can copy and use for any topic moving forward:

Master Prompt Template
> I am a 3rd-year engineering student at EJUST in a team of 5 for a weekly Seminar course. I need you to generate my portion of our weekly assignment based on the topic I provide.
> deliverables required:
> * Report: A technically accurate report based on the topic. (I will specify the page count and required details each time).
> * PowerPoint Content: Extremely minimal and simple slide designs. Include only headers and recommended photos/videos/diagrams—no long text blocks or bullet-heavy slides, as I will explain the details verbally.
> * Presentation Script: A 2.5-minute script (~320–350 words) structured for a clear, engaging delivery.
> Slide Design & Formatting Rules:
> * Background: Solid white background across all slides.
> * Title Placement: Titles consistently anchored in the exact same location on every slide (top-left).
> * Typography: Clear, highly readable, large sans-serif font.
> * Reference QR Code Space: Leave empty, clear space in the top-right corner of content slides so I can insert QR codes linking to reference sources.
> Topic for this week: [Insert Topic Name Here]
> Report Details / Page Count: [Insert Page Count & Specific Requirements Here]""",
        "engineering_verdict": "<strong>ACCEPTED.</strong> This operationalized our workflow, ensuring that every team member (Ezak, Hassan, Farouk, etc.) produced outputs that aligned with the same E-JUST engineering standards and slide formatting rules."
    }
]


# ==========================================
# 3. STRUCTURAL LAYOUT: SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #3D5A80;'>NCM Prompt Architecture</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="disclaimer-box">
            <strong>Academic Disclaimer:</strong><br><br>
            AI was utilized strictly as an assistive tool for syntactical formatting, preliminary ideation, and rapid drafting under rigorous human setup. All final technical parameters, engineering conclusions, and structural outcomes were independently validated and heavily modified by the student team.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Navigation Menu
    selected_phase = st.radio(
        "Select Project Phase Filter:",
        ("Phase 1: Presentation Ideation", 
         "Phase 2: LaTeX Architecture & Report Formatting", 
         "Phase 3: Content Refinement")
    )


# ==========================================
# 4. STRUCTURAL LAYOUT: MAIN CONTENT AREA
# ==========================================
st.markdown(f"<h2>{selected_phase}</h2>", unsafe_allow_html=True)
st.markdown("Review the prompt engineering artifacts and precise engineering verdicts for the selected phase below.")
st.markdown("---")

# Filter data based on selected phase
filtered_prompts = [p for p in prompt_data if p["phase"] == selected_phase]

if not filtered_prompts:
    st.info("No prompts recorded for this phase yet. Select another phase from the sidebar.")
else:
    # Render Cards (using expander)
    for i, item in enumerate(filtered_prompts):
        # Default first item to expanded
        is_first = (i == 0)
        
        with st.expander(f"📌 {item['title']}", expanded=is_first):
            
            # Objective
            st.markdown(f"**Objective:** {item['objective']}")
            
            # Raw Prompt
            st.markdown("**Raw Prompt:**")
            st.code(item['raw_prompt'], language="markdown")
            
            # Engineering Verdict
            st.markdown(
                f"""
                <div class="verdict-box">
                    {item['engineering_verdict']}
                </div>
                """,
                unsafe_allow_html=True
            )
