#!/usr/bin/env python3
"""
GPU-Accelerated Chapter Processing Script
Processes physics textbook chapters using GPU acceleration on RunPod.
"""

import os
import sys
import time
from pathlib import Path

# Enable GPU acceleration
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Use first GPU
os.environ['OMP_NUM_THREADS'] = '2'       # Reduce CPU threading
os.environ['MKL_NUM_THREADS'] = '2'       # Reduce CPU threading
os.environ['NUMEXPR_MAX_THREADS'] = '2'   # Reduce CPU threading

# Additional GPU optimizations
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'  # Optimize GPU memory

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from physics_content.rag_system import RAGSystem, RAG_ANYTHING_AVAILABLE

def main():
    print("🚀 GPU-Accelerated Chapter Processing Started")
    print("=" * 50)
    
    # Check if CUDA is available
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✅ CUDA available: {torch.cuda.get_device_name(0)}")
            print(f"   GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
        else:
            print("⚠️  CUDA not available, using CPU processing")
    except ImportError:
        print("⚠️  PyTorch not installed, using CPU processing")
    
    if not RAG_ANYTHING_AVAILABLE:
        print("❌ RAG-Anything is not available. Please check your installation.")
        sys.exit(1)

    # Initialize RAG system
    try:
        rag = RAGSystem()
        print("✅ RAG System initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize RAG System: {e}")
        sys.exit(1)

    # Process all chapters with GPU acceleration
    try:
        print("\n챕 Starting GPU-accelerated processing of all chapters...")
        stats = rag.build_index()  # This processes all chapters one by one
        
        print("\n" + "="*50)
        print("🎯 GPU PROCESSING COMPLETE!")
        print("="*50)
        print(f"📊 Final Statistics:")
        print(f"   ✅ Successfully Processed: {stats['processed']} chapters")
        print(f"   ⏭️ Already Completed:    {stats['skipped']} chapters")
        print(f"   ❌ Failed:               {stats['failed']} chapters")
        print(f"   ⏱️ Total Time:           {stats['total_time']:.1f} seconds")
        print(f"   📈 Average Time/Chapter: {stats['total_time']/(stats['processed'] or 1):.1f} seconds")
        
        if stats['failed_files']:
            print(f"\n❌ Failed Chapters:")
            for filename in stats['failed_files']:
                print(f"   - {filename}")
                
        if stats['processed'] > 0:
            print(f"\n✅ Processing completed successfully!")
            print("You can now query the processed chapters using the RAG system.")
        else:
            print("\nℹ️  No new chapters were processed.")
            print("All chapters appear to be already processed.")
            
    except KeyboardInterrupt:
        print("\n⚠️  Processing interrupted by user.")
        print("Progress has been saved. You can resume by running this script again.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error during processing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()