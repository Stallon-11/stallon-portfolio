import reflex as rx
from stallon_portfolio.stallon_portfolio import index

def test_portfolio_rendering():
    """Verify the stateless portfolio page contains core CV elements."""
    
    # Generate the page component
    page = index()
    
    # Reflex components compile down to dictionaries/strings for the frontend
    compiled_output = str(page)
    
    # 1. Test that your name renders
    assert "Stallon Fernandes" in compiled_output
    
    # 2. Test that your professional title renders
    assert "AI & Machine Learning Engineer" in compiled_output
    
    # 3. Test that key projects are listed
    assert "Sympto Medical Diagnosis Assistant" in compiled_output
    assert "TfL Knowledge Graph Architecture" in compiled_output

    # 4. Verify the page is wrapped in a layout container (VStack/Container)
    assert isinstance(page, rx.Component)