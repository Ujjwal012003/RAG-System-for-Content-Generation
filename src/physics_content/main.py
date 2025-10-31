#!/usr/bin/env python
"""
Physics Content Generation - Main Entry Point
Generates Class 12 Physics chapters from processed RAG data
"""

import sys
import warnings
import json
from datetime import datetime
from pathlib import Path
from physics_content.crew import PhysicsContentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Define 5 chapters mapped to processed PDFs
CHAPTERS_TO_GENERATE = [
    {"chapter_number": "1", "chapter_name": "Electric_Charges_and_Fields"},
    {"chapter_number": "2", "chapter_name": "Electrostatic_Potential_and_Capacitance"},
    {"chapter_number": "3", "chapter_name": "Current_Electricity"},
    {"chapter_number": "4", "chapter_name": "Moving_Charges_and_Magnetism"},
    {"chapter_number": "5", "chapter_name": "Magnetism_and_Matter"}
]


def ensure_dirs(chapter_number: str):
    """Create necessary artifact directories"""
    directories = ["research", "index", "content", "enhanced", "examples_bank"]
    for sub in directories:
        Path(f"artifacts/{sub}/{chapter_number}").mkdir(parents=True, exist_ok=True)


def save_checkpoint(chapter_number: str, status: str, error: str = None):
    """Save generation checkpoint for recovery"""
    checkpoint_file = Path(f"artifacts/checkpoint_{chapter_number}.json")
    checkpoint_data = {
        "chapter_number": chapter_number,
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "error": error
    }
    with open(checkpoint_file, 'w') as f:
        json.dump(checkpoint_data, f, indent=2)


def run_single_chapter(chapter_number: str, chapter_name: str):
    """
    Generate content for a single chapter using RAG-powered agents
    """
    inputs = {
        'chapter_number': chapter_number,
        'chapter_name': chapter_name,
        'current_year': str(datetime.now().year)
    }
    
    ensure_dirs(chapter_number)
    
    print("\n" + "="*80)
    print(f"🚀 GENERATING CHAPTER {chapter_number}: {chapter_name.replace('_', ' ')}")
    print("="*80)
    print(f"📚 Source: Processed chapters in rag_storage/lightrag/")
    print(f"🔍 Method: RAG-based retrieval (NO internet search)")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")
    
    start_time = datetime.now()
    
    try:
        # Initialize and run crew
        crew_instance = PhysicsContentCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)
        
        # Calculate duration
        duration = (datetime.now() - start_time).total_seconds()
        
        # Check if output file was created (even if crew reported error)
        output_file = Path(f"class_12_physics_chapter_{chapter_number}_{chapter_name}.md")
        
        if output_file.exists():
            # Print success summary
            print("\n" + "="*80)
            print(f"✅ SUCCESS: Chapter {chapter_number} completed!")
            print("="*80)
            print(f"⏱️ Duration: {duration/60:.1f} minutes ({duration:.0f} seconds)")
            print(f"📄 Output: {output_file.name}")
            print(f"📏 File Size: {output_file.stat().st_size / 1024:.1f} KB")
            
            # Print RAG tool statistics
            try:
                from tools.custom_tool import PhysicsRAGTool
                stats = PhysicsRAGTool.get_stats()
                print(f"\n📊 RAG Tool Statistics:")
                print(f"   Total Queries: {stats['total_queries']}")
                print(f"   Cache Hits: {stats['cache_hits']} ({stats['cache_hit_rate']})")
                print(f"   Estimated Cost: {stats['estimated_cost']}")
            except:
                pass
            
            print("="*80 + "\n")
            
            # Save success checkpoint
            save_checkpoint(chapter_number, "completed")
            
            return True
        else:
            # File not created - actual failure
            print("\n" + "="*80)
            print(f"❌ ERROR: Chapter {chapter_number} failed!")
            print("="*80)
            print(f"⏱️ Failed after: {duration/60:.1f} minutes")
            print(f"❌ Output file not created: {output_file.name}")
            print("="*80 + "\n")
            
            save_checkpoint(chapter_number, "failed", "Output file not created")
            return False
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Generation interrupted by user!")
        save_checkpoint(chapter_number, "interrupted", "User cancelled")
        return False
        
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        
        # Check if file was created despite the error
        output_file = Path(f"class_12_physics_chapter_{chapter_number}_{chapter_name}.md")
        
        if output_file.exists():
            # File was created, just report warning
            print("\n" + "="*80)
            print(f"⚠️ WARNING: Chapter {chapter_number} completed with warnings!")
            print("="*80)
            print(f"⏱️ Duration: {duration/60:.1f} minutes")
            print(f"⚠️ Warning: {str(e)}")
            print(f"📄 Output file created: {output_file.name}")
            print(f"📏 File Size: {output_file.stat().st_size / 1024:.1f} KB")
            print(f"💡 Chapter generated successfully despite error in post-processing")
            print("="*80 + "\n")
            
            save_checkpoint(chapter_number, "completed_with_warnings", str(e))
            return True
        else:
            # Actual failure - no file created
            print("\n" + "="*80)
            print(f"❌ ERROR: Chapter {chapter_number} failed!")
            print("="*80)
            print(f"⏱️ Failed after: {duration/60:.1f} minutes")
            print(f"❌ Error: {str(e)}")
            print(f"💾 Partial results may be in artifacts/ folder")
            print("="*80 + "\n")
            
            # Save error checkpoint
            save_checkpoint(chapter_number, "failed", str(e))
            
            return False


def run_all_chapters():
    """
    Batch mode: Generate all 5 chapters sequentially
    """
    success_count = 0
    failed_chapters = []
    total_start_time = datetime.now()
    
    print("\n" + "="*80)
    print("🎯 BATCH PROCESSING MODE: Generating 5 Physics Chapters")
    print("="*80)
    print(f"📚 Source: RAG-processed chapters (NCERT + HC Verma)")
    print(f"🚫 External Search: DISABLED")
    print(f"⏰ Started: {total_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")
    
    for idx, chapter_info in enumerate(CHAPTERS_TO_GENERATE, 1):
        print(f"\n{'#'*80}")
        print(f"### CHAPTER {idx}/5 ###")
        print(f"{'#'*80}\n")
        
        success = run_single_chapter(
            chapter_info['chapter_number'],
            chapter_info['chapter_name']
        )
        
        if success:
            success_count += 1
        else:
            failed_chapters.append(chapter_info['chapter_number'])
        
        # Brief pause between chapters
        if idx < len(CHAPTERS_TO_GENERATE):
            import time
            print("\n⏸️ Pausing 5 seconds before next chapter...\n")
            time.sleep(5)
    
    # Final summary
    total_duration = (datetime.now() - total_start_time).total_seconds()
    
    print("\n" + "="*80)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*80)
    print(f"✅ Successfully Generated: {success_count}/5 chapters")
    print(f"⏱️ Total Duration: {total_duration/60:.1f} minutes ({total_duration/3600:.2f} hours)")
    
    if failed_chapters:
        print(f"❌ Failed Chapters: {', '.join(failed_chapters)}")
        print(f"💡 Tip: Check artifacts/checkpoint_*.json for error details")
    else:
        print("🎉 ALL CHAPTERS GENERATED SUCCESSFULLY!")
    
    # Print aggregate statistics
    try:
        from tools.custom_tool import PhysicsRAGTool
        stats = PhysicsRAGTool.get_stats()
        print(f"\n📊 Total RAG Statistics:")
        print(f"   Total Queries: {stats['total_queries']}")
        print(f"   Cache Hit Rate: {stats['cache_hit_rate']}")
        print(f"   Total Estimated Cost: {stats['estimated_cost']}")
    except:
        pass
    
    print("="*80 + "\n")


def run():
    """
    Interactive mode: Generate single chapter
    """
    print("\n" + "="*80)
    print("📚 Physics Content Generator - Interactive Mode")
    print("="*80 + "\n")
    
    if len(sys.argv) >= 3:
        chapter_number = sys.argv[1].strip()
        chapter_name = "_".join(sys.argv[2:]).strip().replace(" ", "_")
    else:
        print("Available chapters:")
        for ch in CHAPTERS_TO_GENERATE:
            print(f"  {ch['chapter_number']}. {ch['chapter_name'].replace('_', ' ')}")
        print()
        
        chapter_number = input("Enter chapter number (1-5): ").strip()
        chapter_name = input("Enter chapter name: ").strip().replace(" ", "_")
    
    run_single_chapter(chapter_number, chapter_name)


def train():
    """Training mode placeholder"""
    print("⚠️ Training mode not implemented in this version")
    print("💡 Use 'python main.py' for interactive mode")
    print("💡 Use 'python main.py batch' for batch processing")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        
        if mode == "batch":
            # Batch mode: Generate all 5 chapters
            run_all_chapters()
        elif mode in {"train", "replay", "test"}:
            # Legacy modes
            train()
        else:
            # Single chapter mode with args
            run()
    else:
        # Interactive mode
        run()
