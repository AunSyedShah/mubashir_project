# Quick Snacks Website - Technical Documentation

## API Documentation & Design Specifications

### Component Library Documentation

#### Navigation Component
```html
<!-- Standard Navigation Structure -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="images/logo bg.png" width="120" height="120" alt="Quick Snacks Logo">
            <b>Quick Snacks</b>
        </a>
        <button class="navbar-toggler" type="button" 
                data-bs-toggle="collapse" 
                data-bs-target="#navbarSupportedContent">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <!-- Navigation items -->
            </ul>
        </div>
    </div>
</nav>
```

**Properties:**
- `logo-width`: 120px (fixed)
- `logo-height`: 120px (fixed)  
- `responsive-breakpoint`: lg (992px)
- `color-scheme`: light theme

#### Product Card Component
```html
<!-- Standard Product Card Structure -->
<div class="card">
    <img src="images/product.jpg" alt="Product Name">
    <div class="card-content">
        <h3><b>Product Title</b></h3>
        <p>Product description text...</p>
        <p class="price">Pkr [amount]</p>
    </div>
</div>
```

**CSS Styling:**
```css
.card {
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.card-content {
    padding: 1.5rem;
}

.price {
    color: orangered;
    font-weight: bold;
    font-size: 1.2rem;
}
```

### CSS Architecture

#### Color Variables
```css
:root {
    --primary-color: orangered;
    --secondary-color: #f8f9fa;
    --accent-color: red;
    --text-dark: #333333;
    --text-light: #666666;
    --white: #ffffff;
    --shadow: rgba(0, 0, 0, 0.1);
}
```

#### Typography Scale
```css
:root {
    --font-primary: 'Edu AU VIC WA NT Arrows', Arial, sans-serif;
    --font-accent: 'Permanent Marker', cursive;
    
    --font-size-xs: 0.75rem;    /* 12px */
    --font-size-sm: 0.875rem;   /* 14px */
    --font-size-base: 1rem;     /* 16px */
    --font-size-lg: 1.125rem;   /* 18px */
    --font-size-xl: 1.25rem;    /* 20px */
    --font-size-2xl: 1.5rem;    /* 24px */
    --font-size-3xl: 1.875rem;  /* 30px */
    --font-size-4xl: 2.25rem;   /* 36px */
}
```

#### Responsive Breakpoints
```css
/* Mobile First Approach */
.container {
    width: 100%;
    padding: 0 15px;
}

/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) {
    .container { max-width: 540px; }
}

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) {
    .container { max-width: 720px; }
}

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {
    .container { max-width: 960px; }
}

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) {
    .container { max-width: 1140px; }
}
```

### JavaScript Functions

#### Carousel Initialization
```javascript
// Initialize Bootstrap Carousel
document.addEventListener('DOMContentLoaded', function() {
    const carousel = new bootstrap.Carousel(document.querySelector('#carouselExampleCaptions'), {
        interval: 5000,
        wrap: true,
        pause: 'hover'
    });
});
```

#### Mobile Menu Toggle
```javascript
// Mobile navigation enhancement
function toggleMobileMenu() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navbarToggler.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });
}
```

#### Smooth Scrolling Implementation
```javascript
// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
```

### Database Schema (Future Implementation)

#### Products Table
```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    category_id INT,
    image_url VARCHAR(500),
    nutritional_info JSON,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### Categories Table
```sql
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    image_url VARCHAR(500),
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);
```

#### Orders Table
```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(20),
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'confirmed', 'processing', 'delivered', 'cancelled') DEFAULT 'pending',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_address TEXT
);
```

### Performance Optimization Guidelines

#### Image Optimization
```javascript
// Lazy loading implementation
const lazyImages = document.querySelectorAll('img[data-src]');
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

lazyImages.forEach(img => imageObserver.observe(img));
```

#### CSS Optimization
```css
/* Critical CSS - Inline in HTML head */
body { 
    font-family: system-ui, -apple-system, sans-serif; 
    margin: 0; 
    line-height: 1.6;
}

.navbar { 
    background: #f8f9fa; 
    padding: 0.5rem 1rem; 
}

/* Non-critical CSS - Load asynchronously */
@media print {
    /* Print styles */
}
```

### Security Guidelines

#### Input Sanitization
```javascript
// Form input sanitization
function sanitizeInput(input) {
    return input
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');
}

// Email validation
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
```

#### Content Security Policy
```html
<!-- Add to HTML head -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://code.jquery.com;
               style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com;
               font-src 'self' https://fonts.gstatic.com;
               img-src 'self' data:;">
```

### Testing Specifications

#### Unit Testing Template
```javascript
// Jest testing framework example
describe('Product Card Component', () => {
    test('should render product information correctly', () => {
        const product = {
            name: 'Greek Yogurt with Berries',
            price: 2700,
            description: 'Healthy yogurt snack'
        };
        
        const card = createProductCard(product);
        expect(card.querySelector('h3').textContent).toBe(product.name);
        expect(card.querySelector('.price').textContent).toBe(`Pkr ${product.price}`);
    });
    
    test('should handle missing product data gracefully', () => {
        const incompleteProduct = { name: 'Test Product' };
        const card = createProductCard(incompleteProduct);
        expect(card).toBeDefined();
        expect(card.querySelector('.price').textContent).toBe('Price not available');
    });
});
```

#### Cross-Browser Testing Checklist
- [ ] Chrome (latest 2 versions)
- [ ] Firefox (latest 2 versions)  
- [ ] Safari (latest 2 versions)
- [ ] Edge (latest 2 versions)
- [ ] Mobile Chrome (Android)
- [ ] Mobile Safari (iOS)

#### Performance Testing Metrics
```javascript
// Performance measurement
function measurePageLoad() {
    window.addEventListener('load', function() {
        const perfData = performance.getEntriesByType('navigation')[0];
        console.log('Page Load Time:', perfData.loadEventEnd - perfData.fetchStart + 'ms');
        console.log('DOM Content Loaded:', perfData.domContentLoadedEventEnd - perfData.fetchStart + 'ms');
        console.log('First Paint:', performance.getEntriesByType('paint')[0].startTime + 'ms');
    });
}
```

### Deployment Checklist

#### Pre-Deployment
- [ ] Fix all absolute path references
- [ ] Optimize and compress images
- [ ] Minify CSS and JavaScript files
- [ ] Test all navigation links
- [ ] Validate HTML markup
- [ ] Check responsive design on all breakpoints
- [ ] Test form submissions
- [ ] Verify social media links

#### Production Configuration
```nginx
# Nginx configuration example
server {
    listen 80;
    server_name quicksnacks.com;
    root /var/www/quicksnacks;
    index home.html;
    
    # Cache static assets
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, no-transform";
    }
    
    # Enable gzip compression
    gzip on;
    gzip_types text/plain text/css application/javascript image/svg+xml;
}
```

#### SEO Optimization
```html
<!-- Essential meta tags for each page -->
<title>Quick Snacks - Healthy Snacks & Smoothies</title>
<meta name="description" content="Discover delicious, healthy snacks and smoothies. Perfect for kids, diet-conscious individuals, and everyone in between.">
<meta name="keywords" content="healthy snacks, smoothies, kids snacks, organic food">
<meta name="author" content="Quick Snacks">

<!-- Open Graph tags -->
<meta property="og:title" content="Quick Snacks - Healthy Snacks & Smoothies">
<meta property="og:description" content="Discover delicious, healthy snacks and smoothies.">
<meta property="og:image" content="images/logo bg.png">
<meta property="og:url" content="https://quicksnacks.com">

<!-- Twitter Card tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Quick Snacks - Healthy Snacks & Smoothies">
<meta name="twitter:description" content="Discover delicious, healthy snacks and smoothies.">
```

This technical documentation provides comprehensive specifications for developers working on the Quick Snacks website project, covering everything from component structures to deployment considerations.
