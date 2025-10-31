"""
Unit tests for job search system
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from advanced_job_search import JobSearchEngine, UserProfile, JobListing


class TestUserProfile:
    """Test UserProfile dataclass"""
    
    def test_profile_creation(self):
        """Test creating a user profile"""
        profile = UserProfile(
            name="Test User",
            email="test@example.com",
            target_roles=["ai engineer"],
            skills=["python", "pytorch"],
            experience_level="junior",
            locations=["remote"],
            remote_preference=True
        )
        
        assert profile.name == "Test User"
        assert "ai engineer" in profile.target_roles
        assert "python" in profile.skills
        assert profile.remote_preference is True


class TestJobListing:
    """Test JobListing dataclass"""
    
    def test_job_creation(self):
        """Test creating a job listing"""
        job = JobListing(
            title="AI Engineer",
            company="Test Co",
            location="Remote",
            url="https://example.com/job",
            description="AI engineer position",
            platform="test"
        )
        
        assert job.title == "AI Engineer"
        assert job.match_score == 0.0  # Default
        assert len(job.required_skills) == 0  # Default empty list


class TestJobSearchEngine:
    """Test JobSearchEngine"""
    
    def test_engine_initialization(self):
        """Test initializing search engine"""
        profile = UserProfile(
            name="Test",
            email="test@test.com",
            target_roles=["ai engineer"],
            skills=["python"],
            experience_level="junior",
            locations=["remote"],
            remote_preference=True
        )
        
        engine = JobSearchEngine(profile)
        assert engine.profile == profile
        assert len(engine.jobs) == 0


class TestMatchScoring:
    """Test job matching and scoring"""
    
    def test_exact_title_match(self):
        """Test scoring for exact title match"""
        profile = UserProfile(
            name="Test",
            email="test@test.com",
            target_roles=["ai engineer"],
            skills=["python", "pytorch"],
            experience_level="junior",
            locations=["remote"],
            remote_preference=True
        )
        
        engine = JobSearchEngine(profile)
        
        job = JobListing(
            title="AI Engineer",
            company="Test Co",
            location="Remote",
            url="https://example.com",
            description="python pytorch machine learning",
            platform="test"
        )
        
        score = engine._calculate_match_score(job)
        assert score >= 35  # Title match should give at least 35 points
        assert score <= 100
    
    def test_skills_match(self):
        """Test scoring when skills match"""
        profile = UserProfile(
            name="Test",
            email="test@test.com",
            target_roles=["ai engineer"],
            skills=["python", "pytorch", "llm"],
            experience_level="junior",
            locations=["remote"],
            remote_preference=True
        )
        
        engine = JobSearchEngine(profile)
        
        job = JobListing(
            title="AI Engineer",
            company="Test Co",
            location="Remote",
            url="https://example.com",
            description="Looking for someone with python pytorch llm experience",
            platform="test"
        )
        
        score = engine._calculate_match_score(job)
        assert score > 50  # Should have high match with skills


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

