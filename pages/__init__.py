# Make pages directory a package
from pages.home import render_home_page
from pages.monitor import render_monitor_page
from pages.about import render_about_page

__all__ = ['render_home_page', 'render_monitor_page', 'render_about_page']
