
import os

# Define categories with associated keywords, resume filenames, and taglines
JOB_CATEGORIES = {
    "Software Engineering": {
        "keywords": [
            "software engineer", "software developer", "backend", "frontend", 
            "full stack", "fullstack", "web developer", "application developer"
        ],
        "resume_file": "software.pdf", # Mapping to existing file
        "tagline": "Software Engineering Intern | Backend & Systems Focused"
    },
    "AI / ML": {
        "keywords": [
            "ai", "artificial intelligence", "machine learning", "ml engineer", 
            "deep learning", "data scientist"
        ],
        "resume_file": "AI.pdf", # Kept as is, user might need to ensure this exists or I should use a default
        "tagline": "AI & Machine Learning Intern | Applied Intelligence Systems"
    },
    "Cybersecurity – Offensive": {
        "keywords": [
            "penetration tester", "pentest", "red team", "offensive security", 
            "exploit development"
        ],
        "resume_file": "pentesting.pdf",
        "tagline": "Offensive Security Intern | Red Team & Exploit Analysis"
    },
    "Cybersecurity – Defensive / SOC": {
        "keywords": [
            "soc", "security operations", "blue team", "security analyst", 
            "incident response", "threat detection"
        ],
        "resume_file": "soc.pdf",
        "tagline": "Security Operations Intern | Detection & Threat Response"
    },
    "Security Research": {
        "keywords": [
            "security researcher", "vulnerability research", "reverse engineering", 
            "malware analysis"
        ],
        "resume_file": "research_security.pdf",
        "tagline": "Security Research Intern | Vulnerability & Exploit Analysis"
    },
    "Cloud / Network": {
        "keywords": [
            "azure devops", "cloud engineer", "network engineer", "devops", "infrastructure", 
            "cloud security"
        ],
        "resume_file": "cloud.pdf",
        "tagline": "Cloud & Infrastructure Intern | Secure Distributed Systems"
    }
}

import re

def classify_job(job_title: str):
    """
    Classifies a job based on its title using keyword matching with word boundaries.
    
    Args:
        job_title (str): The title of the job.
        
    Returns:
        dict: A dictionary containing category, resume_file, and tagline if a match is found.
              Returns None if no match is found.
    """
    title_lower = job_title.lower()
    
    for category, details in JOB_CATEGORIES.items():
        for keyword in details["keywords"]:
            # Use regex to check for whole word matches
            # Escape keyword to handle special characters effectively, though mostly simple strings
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            if re.search(pattern, title_lower):
                # Handle specific resume overrides based on keywords if needed
                resume = details["resume_file"]
                if category == "Software Engineering":
                    if "fullstack" in title_lower or "full stack" in title_lower:
                        resume = "fullstack.pdf"
                    else:
                         resume = "software.pdf"
                
                elif category == "AI / ML":
                     # No specific "ML.pdf" found in default/, so sticking to AI.pdf or fallback
                     # If user provides ML.pdf in root, it will use that.
                     if "machine learning" in title_lower or "ml" in title_lower:
                         resume = "ML.pdf"
                
                elif category == "Cybersecurity – Defensive / SOC" and ("blue team" in title_lower):
                    resume = "blueteam.pdf" 
                    # Note: blueteam.pdf exists in root based on Step 181

                return {
                    "category": category,
                    "resume_file": resume,
                    "tagline": details["tagline"]
                }
    
    return None
