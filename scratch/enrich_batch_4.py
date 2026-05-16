import json
import os

# Batch 4 Enriched Data
BATCH_4 = {
    "nextjs_console_hooks_usechat_ts": {
        "functionDesc": "Primary React hook managing conversational state, message history, and LLM streaming.",
        "detailedLogic": "Implements a multi-session state machine with local persistence. Orchestrates typewriter-style streaming and integrates with the Intent Router for dynamic UI transitions. Handles attachment processing and content classification triggers.",
        "importance": "CRITICAL"
    },
    "nextjs_console_hooks_useagenticstream_ts": {
        "functionDesc": "Specialized hook for managing and visualizing the lifecycle of autonomous AI agent workflows.",
        "detailedLogic": "Wraps a pure reducer-based state machine to track agent transitions (Reasoning -> Tool Use). Provides real-time observability into AI reasoning steps during multi-modal tasks.",
        "importance": "HIGH"
    },
    "nextjs_console_hooks_useintentrouter_ts": {
        "functionDesc": "Intelligent navigation hook that routes users to app features based on AI-detected conversational intent.",
        "detailedLogic": "Translates assistant replies into navigational commands using a semantic mapping layer. Supports context banners to maintain continuity across page transitions.",
        "importance": "HIGH"
    },
    "nextjs_console_hooks_usecanvaspersistence_ts": {
        "functionDesc": "Manages local and remote persistence for the interactive system graph and node layouts.",
        "detailedLogic": "Implements a debounced auto-save mechanism to localStorage. Synchronizes canvas state (node positions/zoom) with the backend for persistent multi-session exploration.",
        "importance": "MEDIUM"
    },
    "app_utils_id_generator_py": {
        "functionDesc": "Centralized utility for generating secure, prefixed identifiers (IDs) for all system entities.",
        "detailedLogic": "Utilizes Python's 'secrets' module for cryptographic entropy. Standardizes ID formats (prefix_randompart) for Blueprints and Diagnostics to ensure global traceability.",
        "importance": "MEDIUM"
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
        if node_id in BATCH_4:
            updates = BATCH_4[node_id]
            node.update(updates)
            updated_count += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully enriched {updated_count} nodes in Batch 4.")

if __name__ == "__main__":
    enrich_graph()
