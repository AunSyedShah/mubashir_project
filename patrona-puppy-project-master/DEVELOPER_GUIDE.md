# Patrona Puppy Website - Developer Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technical Architecture](#technical-architecture)
3. [Development Setup](#development-setup)
4. [File Structure](#file-structure)
5. [Code Standards](#code-standards)
6. [Deployment](#deployment)
7. [Maintenance](#maintenance)
8. [Troubleshooting](#troubleshooting)

## Project Overview

### Project Details
- **Project Name**: Patrona Puppy Website
- **Type**: Static HTML/CSS Website
- **Purpose**: Dog breed encyclopedia and puppy care resource
- **Target Audience**: Dog enthusiasts, potential dog owners, pet care seekers
- **Technology Stack**: HTML5, CSS3, Bootstrap 5, JavaScript

### Key Features
- Responsive design for all devices
- Interactive image carousels
- Dropdown navigation menus
- Multi-page breed information
- Contact forms
- FAQ system

## Technical Architecture

### Frontend Technologies

#### HTML5
- Semantic HTML structure
- Accessibility-compliant markup
- SEO-optimized meta tags
- Form validation attributes

#### CSS3
- Custom stylesheets for each page
- Responsive design principles
- Flexbox and Grid layouts
- CSS animations and transitions

#### Bootstrap 5.0.2
- **CDN**: `https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css`
- Responsive grid system
- Pre-built components
- Utility classes
- JavaScript components

#### FontAwesome 6.7.2
- **CDN**: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css`
- Icon library
- Scalable vector icons
- Cross-browser compatibility

### Browser Support Matrix
| Browser | Version | Support Level |
|---------|---------|---------------|
| Chrome | 80+ | Full Support |
| Firefox | 75+ | Full Support |
| Safari | 13+ | Full Support |
| Edge | 80+ | Full Support |
| IE | 11 | Limited Support |

## Development Setup

### Prerequisites
- Text editor or IDE (VS Code, Sublime Text, Atom)
- Modern web browser for testing
- Local web server (optional but recommended)
- Git for version control

### Local Development Environment

#### Option 1: Simple HTTP Server (Python)
```bash
# Navigate to project directory
cd patrona-puppy-project-master

# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Access at: http://localhost:8000
```

#### Option 2: Node.js HTTP Server
```bash
# Install http-server globally
npm install -g http-server

# Navigate to project directory
cd patrona-puppy-project-master

# Start server
http-server -p 8000

# Access at: http://localhost:8000
```

#### Option 3: VS Code Live Server Extension
1. Install "Live Server" extension
2. Right-click on `home.html`
3. Select "Open with Live Server"

## File Structure

```
patrona-puppy-project-master/
├── home.html                    # Main landing page
├── breeds.html                  # Dog breeds main page
├── breeds1.html                 # Breeds page 1
├── breeds2.html                 # Breeds page 2
├── breeds3.html                 # Breeds page 3
├── breeds4.html                 # Breeds page 4
├── behaviour.html               # Puppy care and behavior
├── food&nutrition.html          # Nutrition information
├── FAQ.html                     # Frequently asked questions
├── contactus.html              # Contact form and info
├── blogs1.html                 # Blog page 1
├── blogs2.html                 # Blog page 2
├── blogs3.html                 # Blog page 3
├── beauty.html                 # Beauty and grooming
├── asia.html                   # Regional content
├── treats.html                 # Dog treats information
│
├── CSS/                        # Stylesheets directory
│   ├── home.css               # Home page styles
│   ├── breeds.css             # Breeds pages styles
│   ├── behaviour.css          # Puppy care styles
│   ├── FAQ.css                # FAQ page styles
│   └── contactus.css          # Contact page styles
│
├── img/                       # Images directory
│   ├── logo.jpeg              # Site logo
│   ├── homeslider1.jpg        # Homepage slider images
│   ├── homeslider2.jpg
│   ├── homeslider3.jpg
│   ├── [breed-images].jpg     # Various breed photos
│   └── [other-images]         # Additional site images
│
├── aboutdogs/                 # Dog breed detail pages
│   ├── gallery.html           # Photo gallery
│   ├── golden.html            # Golden Retriever details
│   ├── german.html            # German Shepherd details
│   ├── australian.html        # Australian Shepherd details
│   ├── pomeranian.html        # Pomeranian details
│   ├── siberian.html          # Siberian Husky details
│   ├── bulldog.html           # Bulldog details
│   ├── boxer.html             # Boxer details
│   ├── labrador.html          # Labrador details
│   ├── icelandic.html         # Icelandic Sheepdog details
│   ├── canecarso.html         # Cane Corso details
│   ├── Ffinnishspitz.html     # Finnish Spitz details
│   ├── PITBUL.HTML            # Pitbull details
│   └── img/                   # Breed-specific images
│
├── USER_GUIDE.md              # User documentation
├── DEVELOPER_GUIDE.md         # This developer guide
└── README.md                  # Project overview
```

## Code Standards

### HTML Guidelines

#### Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title - Petrona Puppy</title>
    
    <!-- External CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="CSS/page-specific.css">
</head>
<body>
    <!-- Content -->
</body>
</html>
```

#### Navigation Structure
```html
<nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
        <a class="navbar-brand d-flex align-items-center" href="home.html">
            <img src="img/logo.jpeg" alt="Logo" class="img-fluid logo">
            <span class="ms-2 site-title">PETRONA PUPPY</span>
        </a>
        <!-- Navigation items -->
    </div>
</nav>
```

### CSS Guidelines

#### File Organization
- One CSS file per page/section
- Consistent naming conventions
- Organized by component hierarchy
- Comments for complex styles

#### CSS Structure
```css
/* Reset and Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Component Styles */
.navbar {
    /* Navbar styles */
}

.carousel {
    /* Carousel styles */
}

/* Responsive Design */
@media (max-width: 768px) {
    /* Mobile styles */
}
```

### Image Guidelines

#### Image Optimization
- **Format**: JPEG for photos, PNG for graphics with transparency
- **Size**: Optimize for web (compress without quality loss)
- **Naming**: Descriptive, lowercase, hyphens for spaces
- **Alt Text**: Always include meaningful alt attributes

#### Image Dimensions
- **Hero Images**: 1920x1080px recommended
- **Card Images**: 400x300px recommended
- **Logo**: SVG preferred, or high-resolution PNG

### Responsive Design Standards

#### Breakpoints (Bootstrap)
- **xs**: <576px (Extra small devices)
- **sm**: ≥576px (Small devices)
- **md**: ≥768px (Medium devices)
- **lg**: ≥992px (Large devices)
- **xl**: ≥1200px (Extra large devices)

#### Mobile-First Approach
```css
/* Mobile styles (default) */
.element {
    width: 100%;
}

/* Tablet and up */
@media (min-width: 768px) {
    .element {
        width: 50%;
    }
}

/* Desktop and up */
@media (min-width: 992px) {
    .element {
        width: 33.333%;
    }
}
```

## Common Issues and Fixes

### Issue Tracking

#### Fixed Issues ✅
1. **Broken Golden Retriever Links**
   - **Problem**: Links pointed to `goldenretriever.html` instead of `golden.html`
   - **Fix**: Updated all navigation links across 12+ files
   - **Files Affected**: All main HTML files

2. **Incorrect Page Titles**
   - **Problem**: Generic or incorrect titles on several pages
   - **Fix**: Updated titles to be descriptive and consistent
   - **Pattern**: "Page Name - Petrona Puppy"

#### Known Issues ⚠️
1. **Absolute Path Usage**
   - **Issue**: Links use absolute paths (`/CSS/`, `/img/`)
   - **Impact**: Won't work when opening files locally
   - **Recommendation**: Convert to relative paths for local compatibility

2. **File Naming Inconsistency**
   - **Issue**: `PITBUL.HTML` uses different case convention
   - **Impact**: Minor, links work correctly
   - **Recommendation**: Standardize to lowercase `.html`

### Path Resolution

#### Current Path Structure (Absolute)
```html
<!-- May not work locally -->
<link rel="stylesheet" href="/CSS/home.css">
<img src="/img/logo.jpeg" alt="Logo">
<a href="/aboutdogs/golden.html">Golden Retriever</a>
```

#### Recommended Path Structure (Relative)
```html
<!-- Works both locally and on server -->
<link rel="stylesheet" href="CSS/home.css">
<img src="img/logo.jpeg" alt="Logo">
<a href="aboutdogs/golden.html">Golden Retriever</a>
```

## Deployment

### Production Deployment

#### Web Server Requirements
- Apache 2.4+ or Nginx 1.18+
- PHP not required (static site)
- HTTPS recommended
- Gzip compression enabled

#### Deployment Steps
1. **Prepare Files**
   ```bash
   # Ensure all files are present
   # Verify image optimization
   # Test all links locally
   ```

2. **Upload to Server**
   ```bash
   # Via FTP, SFTP, or deployment tools
   # Maintain directory structure
   # Set proper file permissions (644 for files, 755 for directories)
   ```

3. **Configure Web Server**
   ```apache
   # .htaccess (Apache)
   DirectoryIndex home.html
   
   # Enable compression
   <IfModule mod_deflate.c>
       AddOutputFilterByType DEFLATE text/html text/css application/javascript
   </IfModule>
   
   # Cache static resources
   <IfModule mod_expires.c>
       ExpiresActive On
       ExpiresByType image/jpeg "access plus 1 month"
       ExpiresByType text/css "access plus 1 week"
   </IfModule>
   ```

#### CDN Integration
- Bootstrap and FontAwesome load from CDN
- Consider local fallbacks for critical resources
- Monitor CDN availability and performance

### Testing Checklist

#### Pre-deployment Testing
- [ ] All pages load correctly
- [ ] Navigation links work
- [ ] Images display properly
- [ ] Forms submit correctly
- [ ] Responsive design works on all devices
- [ ] Cross-browser compatibility verified
- [ ] Page load speeds acceptable
- [ ] SEO meta tags present

#### Post-deployment Testing
- [ ] Live site loads correctly
- [ ] SSL certificate working
- [ ] All CDN resources loading
- [ ] Contact forms sending emails
- [ ] Analytics tracking implemented
- [ ] Search engine indexing allowed

## Performance Optimization

### Image Optimization
```bash
# Compress JPEG images
jpegoptim --size=100k *.jpg

# Optimize PNG images
optipng -o7 *.png

# Convert to WebP for modern browsers
cwebp -q 80 input.jpg -o output.webp
```

### CSS Optimization
```css
/* Minimize CSS files */
/* Remove unused styles */
/* Use efficient selectors */
/* Combine media queries */
```

### Loading Performance
- Minimize HTTP requests
- Use CSS sprites for small icons
- Implement lazy loading for images
- Enable browser caching

## Maintenance

### Regular Tasks

#### Monthly
- [ ] Check all external links
- [ ] Verify CDN resources still available
- [ ] Test contact forms
- [ ] Review analytics data
- [ ] Check for broken images

#### Quarterly
- [ ] Update Bootstrap version if needed
- [ ] Review and update content
- [ ] Performance audit
- [ ] Security scan
- [ ] Backup website files

#### Annually
- [ ] Full content review and update
- [ ] Design refresh consideration
- [ ] User feedback analysis
- [ ] Technology stack review

### Content Management

#### Adding New Breeds
1. Create new HTML file in `aboutdogs/` directory
2. Follow existing template structure
3. Add high-quality breed images to `aboutdogs/img/`
4. Update navigation menus in all files
5. Test all links and functionality

#### Updating Existing Content
1. Backup original files
2. Make changes to content
3. Test locally before deploying
4. Update last modified dates
5. Deploy and verify changes

## Version Control

### Git Workflow
```bash
# Clone repository
git clone [repository-url]

# Create feature branch
git checkout -b fix/broken-links

# Make changes and commit
git add .
git commit -m "Fix: Update Golden Retriever navigation links"

# Push changes
git push origin fix/broken-links

# Create pull request for review
```

### Branching Strategy
- **main/master**: Production-ready code
- **develop**: Integration branch for new features
- **feature/**: New features or major updates
- **fix/**: Bug fixes and minor corrections
- **hotfix/**: Emergency fixes for production

## Security Considerations

### Basic Security Measures
- Regular backups
- Strong server passwords
- HTTPS implementation
- File permission management
- Regular software updates

### Contact Form Security
- Input validation
- CAPTCHA implementation
- Rate limiting
- Spam filtering
- Data sanitization

---

## Support and Resources

### Documentation
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/)
- [FontAwesome Icons](https://fontawesome.com/icons)
- [HTML5 Specification](https://html.spec.whatwg.org/)
- [CSS3 Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)

### Development Tools
- [VS Code](https://code.visualstudio.com/)
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

---

**Last Updated**: August 30, 2025  
**Version**: 1.0  
**Maintained by**: Development Team
