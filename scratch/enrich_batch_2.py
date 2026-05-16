import json
import os

# Batch 2 Enriched Data
BATCH_2 = {
    "nextjs_console_app_layout_tsx": {
        "functionDesc": "Root layout establishing the global console structure, design system, and global state providers.",
        "detailedLogic": "Implements a hierarchical Context Provider pattern (Mode, Router, Locale). Orchestrates the primary flexbox-based shell containing the Sidebar and main scroll area.",
        "importance": "HIGH"
    },
    "nextjs_console_app_console_page_tsx": {
        "functionDesc": "Primary conversational AI interface for multi-modal interactions and real-time assistant responses.",
        "detailedLogic": "Orchestrates complex hook-based state using useChat and useAgenticStream. Features dynamic intent-based routing and a chip-based suggestion system for guided UX.",
        "importance": "CRITICAL"
    },
    "nextjs_console_app_dashboard_page_tsx": {
        "functionDesc": "Central command hub providing a high-level overview of AI readiness and project lifecycles.",
        "detailedLogic": "Aggregates data from multiple diagnostic services. Implements priority-based rendering logic for lifecycle cards (Deep Assessment > Free Scan > Default).",
        "importance": "HIGH"
    },
    "nextjs_console_app_diagnostics_page_tsx": {
        "functionDesc": "Entry point for AI assessments, managing the selection and status of different diagnostic tiers.",
        "detailedLogic": "Integrates with DeepDiagnosticService to provide resume-from-last-point capabilities and real-time status tracking for assessment flows.",
        "importance": "HIGH"
    },
    "nextjs_console_app_blueprint_page_tsx": {
        "functionDesc": "Interactive report viewer for AI System Blueprints, including ROI projections and architecture mapping.",
        "detailedLogic": "Maps complex VPS Bridge responses to structured insights. Implements local versioning for drafts and supports multi-format document exports.",
        "importance": "HIGH"
    },
    "nextjs_console_app_diagnostics_deep_page_tsx": {
        "functionDesc": "Multi-phase wizard for comprehensive deep-dive AI readiness assessments.",
        "detailedLogic": "Implements a phased wizard pattern with debounced persistence. Features a PhaseNavigator and ProgressTracker to guide users through 4 distinct assessment stages.",
        "importance": "HIGH"
    },
    "nextjs_console_app_integrations_page_tsx": {
        "functionDesc": "Management hub for connecting and authenticating third-party service integrations.",
        "detailedLogic": "Supports dual-flow authentication (Manual API vs OAuth via Composio). Features a real-time polling mechanism and connection lifecycle management (Revoke/Re-auth).",
        "importance": "HIGH"
    },
    "nextjs_console_app_roadmap_page_tsx": {
        "functionDesc": "Strategic planning interface visualizing the phased rollout of AI initiatives and KPI targets.",
        "detailedLogic": "Utilizes a custom CSS-based timeline implementation. Manages milestone persistence and integrates with the Aira assistant for interactive roadmap refinement.",
        "importance": "HIGH"
    }
}

def enrich_graph():
    path = 'data/graph.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get('nodes', [])
    updated_count = 0
    
    for node in nodes:
        node_id = node.get('id')
        if node_id in BATCH_2:
            updates = BATCH_2[node_id]
            node.update(updates)
            updated_count += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully enriched {updated_count} nodes in Batch 2.")

if __name__ == "__main__":
    enrich_graph()
