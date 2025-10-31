"""
Tests for Neuro parser
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from run_neuro import NeuroRunner


class TestNeuroParser:
    """Test Neuro file parsing"""
    
    def test_parse_job_search_neuro(self):
        """Test parsing my_job_search.neuro"""
        runner = NeuroRunner()
        
        neuro_content = """
pipeline FindAIPositions {
    goal: "Find prompt engineer and AI engineer jobs"
    target_roles: ["prompt engineer", "ai engineer"]
    locations: ["remote", "US"]
    skills: ["python", "pytorch"]
    actions: [search_job_boards(), match_skills()]
}
"""
        
        pipeline = runner.parse_neuro(neuro_content)
        
        assert pipeline['goal'] == "Find prompt engineer and AI engineer jobs"
        assert "prompt engineer" in pipeline['target_roles']
        assert "remote" in pipeline['locations']
        assert "python" in pipeline['skills']
        assert len(pipeline['actions']) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

