import json
import os

# Batch 1 Enriched Data
BATCH_1 = {
    "nextjs_console_services_deepdiagnostic_ts": {
        "functionDesc": "Core orchestration engine for AI readiness assessments and ROI projections.",
        "detailedLogic": "Implements a Service-layer Singleton pattern with dual-write persistence (Supabase + LocalStorage). Uses industry-aware labor rate mappings and midpoint-range parsing to calculate complex financial ROI and payback periods.",
        "importance": "CRITICAL"
    },
    "vps_bridge_endpoints_js": {
        "functionDesc": "Central API routing hub connecting the frontend to specialized AI services.",
        "detailedLogic": "Middleware-based Express router using Zeroclaw as the primary AI engine. Implements conversation history normalization and onboarding state-rewriting logic to maintain coherence across multi-turn AI interactions.",
        "importance": "CRITICAL"
    },
    "n8n_as_code_service_index_js": {
        "functionDesc": "Orchestrates 'Workflow-as-Code' capabilities for programmatic n8n deployments.",
        "detailedLogic": "Uses a regex-based intent detection engine to map natural language to n8n node schemas. Features a sandbox environment for credential stripping and logic validation before production delivery.",
        "importance": "HIGH"
    },
    "nextjs_console_app_workflows_page_tsx": {
        "functionDesc": "Primary dashboard interface for managing and monitoring automation workflows.",
        "detailedLogic": "Next.js Server Component that integrates real-time status updates with a dynamic workflow management grid. Directly bridges the user UI to the n8n-as-code deployment pipeline.",
        "importance": "HIGH"
    },
    "nextjs_console_components_workflow_workflowcanvas_tsx": {
        "functionDesc": "Interactive visual designer for structural workflow exploration and node inspection.",
        "detailedLogic": "React-based canvas implementation managing complex graph adjacency lists and edge routing. Provides real-time visual feedback for programmatic node configurations.",
        "importance": "MEDIUM"
    },
    "basemodel": {
        "functionDesc": "Global Pydantic base abstraction for all backend data structures and schemas.",
        "detailedLogic": "Provides strict type validation, field aliasing, and serialization logic for the entire Python backend. Serves as the foundation for Blueprint, Diagnostic, and User models.",
        "importance": "CORE"
    },
    "frontend_dashboard_js": {
        "functionDesc": "Standalone dashboard orchestrator for navigation and global UI state management.",
        "detailedLogic": "Vanilla JS modular pattern using a global event-bus for sidebar injection, modal orchestration, and D3-based visualization lifecycle management.",
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
        if node_id in BATCH_1:
            updates = BATCH_1[node_id]
            node.update(updates)
            updated_count += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully enriched {updated_count} nodes in Batch 1.")

if __name__ == "__main__":
    enrich_graph()
