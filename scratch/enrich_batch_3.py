import json
import os

# Batch 3 Enriched Data
BATCH_3 = {
    "app_services_ai_blueprint_generator_py": {
        "functionDesc": "Orchestrates the automated creation of AI System Blueprints from assessment data.",
        "detailedLogic": "Executes a multi-step pipeline: System Naming -> Agent Design -> Workflow Mapping -> Integration Detection. Maps business pain points to specific technical agent capabilities (Trigger/Tool/Pseudo-logic).",
        "importance": "HIGH"
    },
    "app_services_ai_enrichment_py": {
        "functionDesc": "Provides personalized, AI-driven insights and narratives based on diagnostic scores.",
        "detailedLogic": "Implements a 'Graceful Degradation' pattern; attempts LLM-based personalization but falls back to deterministic static content if LLM services time out or fail.",
        "importance": "HIGH"
    },
    "app_services_scoring_service_py": {
        "functionDesc": "Deterministic core engine that calculates AI readiness scores and maturity levels.",
        "detailedLogic": "Maps 12 distinct multi-choice answers to a 0-100 normalized scale. Categorizes organizations into 4 maturity levels using strict range-based classification logic.",
        "importance": "CRITICAL"
    },
    "app_services_blueprint_storage_py": {
        "functionDesc": "Manages persistence, versioning, and retrieval of generated AI blueprints.",
        "detailedLogic": "Handles multi-format storage (JSON/PDF). Implements a semantic versioning system for blueprint iterations and manages tenant-specific storage paths with access control.",
        "importance": "HIGH"
    },
    "app_services_console_service_py": {
        "functionDesc": "Backend processing engine for real-time conversational AI interactions.",
        "detailedLogic": "Orchestrates context assembly, model selection, and reasoning metadata generation. Acts as the primary bridge between UI chat components and LLM providers.",
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
        if node_id in BATCH_3:
            updates = BATCH_3[node_id]
            node.update(updates)
            updated_count += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully enriched {updated_count} nodes in Batch 3.")

if __name__ == "__main__":
    enrich_graph()
