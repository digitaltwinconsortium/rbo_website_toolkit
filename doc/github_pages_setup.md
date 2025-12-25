# GitHub Pages & Custom Domain Setup

Guide for deploying RBO websites to GitHub Pages with custom domains.

## Prerequisites

- GitHub repository with the RBO website code
- Custom domain registered (e.g., `digitaltwins-sg.org`)
- Access to DNS management (this guide covers AWS Route 53)

## Step 1: Enable GitHub Pages

1. Go to your repository **Settings** → **Pages**
2. Under **Build and deployment**:
   - Source: **GitHub Actions**
3. The deploy workflow (`.github/workflows/deploy.yml`) will handle builds

## Step 2: Add CNAME File

Create a `CNAME` file in your repository root with your custom domain:

```
www.yourdomain.org
```

The build script will automatically copy this to the output directory.

## Step 3: Configure DNS

### AWS Route 53 Setup

#### 3a. Open Route 53

1. AWS Console → **Route 53** → **Hosted zones**
2. Click on your domain (e.g., `digitaltwins-sg.org`)

#### 3b. Add CNAME Record for www

Click **Create record**:

| Field | Value |
|-------|-------|
| **Record name** | `www` |
| **Record type** | `CNAME` |
| **Value** | `YOUR-ORG.github.io` |
| **TTL** | `300` |
| **Routing policy** | Simple routing |

Example: For `digitaltwinconsortium` org, value is `digitaltwinconsortium.github.io`

#### 3c. Add A Records for Apex Domain

Click **Create record**:

| Field | Value |
|-------|-------|
| **Record name** | *(leave blank)* |
| **Record type** | `A` |
| **TTL** | `300` |
| **Value** | Enter all 4 IPs (one per line): |

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

#### 3d. (Optional) Add AAAA Records for IPv6

Click **Create record**:

| Field | Value |
|-------|-------|
| **Record name** | *(leave blank)* |
| **Record type** | `AAAA` |
| **TTL** | `300` |
| **Value** | Enter all 4 IPs: |

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

### Other DNS Providers

For other DNS providers (Cloudflare, GoDaddy, Namecheap, etc.), the records are the same:

| Type | Name | Value |
|------|------|-------|
| CNAME | www | `YOUR-ORG.github.io` |
| A | @ | `185.199.108.153` |
| A | @ | `185.199.109.153` |
| A | @ | `185.199.110.153` |
| A | @ | `185.199.111.153` |

## Step 4: Verify in GitHub

1. Go to repository **Settings** → **Pages**
2. Custom domain should show from your CNAME file
3. Wait for DNS check to pass (green checkmark)
4. Enable **Enforce HTTPS**

## Step 5: Verify Deployment

### Check DNS Propagation

```bash
# Check CNAME
dig www.yourdomain.org CNAME

# Check A records  
dig yourdomain.org A
```

Or use [DNS Checker](https://dnschecker.org) for global propagation status.

### Test URLs

After DNS propagates (5-60 minutes typically):

- ✅ `https://www.yourdomain.org` → Your site
- ✅ `https://yourdomain.org` → Redirects to www
- ✅ `https://your-org.github.io/repo-name/` → Redirects to custom domain

## Troubleshooting

### DNS not resolving

- Wait up to 48 hours for full propagation (usually faster)
- Verify records in Route 53 console
- Check for typos in CNAME value

### HTTPS not working

- Ensure DNS is verified in GitHub Pages settings
- HTTPS provisioning can take up to 24 hours
- Check that "Enforce HTTPS" is enabled

### 404 errors

- Verify GitHub Actions workflow completed successfully
- Check that `site/` directory contains built files
- Ensure CNAME file is being copied to output

### Mixed content warnings

- Ensure all asset URLs use `/assets/...` (not `http://...`)
- Check for hardcoded HTTP URLs in content

## Local Development

Custom domain configuration doesn't affect local development:

```bash
python toolkit/build.py
python -m http.server -d site 8888
# Visit http://localhost:8888
```

## References

- [GitHub Pages Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Managing Custom Domain for GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [AWS Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

