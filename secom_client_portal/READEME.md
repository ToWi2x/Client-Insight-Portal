# SECOM Enterprise Client Operations Portal

A secure, full-stack web application designed for enterprise security clients to monitor live hardware status, track support tickets, and analyze active network/physical threats.

## Project Overview

This Proof of Concept (PoC) was built to demonstrate a modern, scalable client dashboard for the security sector. It moves away from static reporting and provides clients with a real-time Operations Center interface.

**Key Features:**
* **Google Single Sign-On (SSO):** Enterprise-grade authentication using OAuth 2.0 via `django-allauth`.
* **Live Hardware Status Grid:** Real-time visualization of site-wide devices (CCTV, Access Control, Firewalls) with automated color-coded health indicators.
* **Threat Analytics:** Interactive Doughnut chart built with `Chart.js` to break down active security alerts by severity (Critical, Warning, Info).
* **Support Metric Tracking:** Data tables tracking system uptime, project health, and monthly resolved IT/Security tickets.

## Technology Stack

* **Backend:** Python, Django 5.x
* **Database:** SQLite (Development) / Ready for PostgreSQL (Production)
* **Authentication:** Django-Allauth (Google Provider / JWT)
* **Frontend:** HTML5, Bootstrap 5, Chart.js

## Dashboard Preview


![SECOM Dashboard Concept](dashboard.png)

## Core Architecture

The database is built on highly relational Django models to link users directly to their localized security infrastructure:

* `ClientOutcome`: Tracks overall project health and uptime metrics.
* `SecurityAlert`: Logs physical and digital breaches with timestamps and resolution tracking.
* `DeviceHealth`: Monitors individual IoT and security hardware across multiple warehouse and office locations.

## Security Implementations

* Isolated Python Virtual Environments for dependency management.
* Cryptography libraries deployed for secure token handling.
* Protected routes utilizing Django's `@login_required` decorators.
* Environment variables abstracted for sensitive Client IDs and Secret Keys.

# SECOM Enterprise Client Operations Portal & IoT Telemetry Gateway

A secure, full-stack web application designed for enterprise security clients. This system provides a central operations center for monitoring live physical hardware status via a dedicated REST API, tracking support tickets, and analyzing active network threats.

## Project Overview

This Proof of Concept (PoC) was built to demonstrate a modern, scalable client dashboard for the security sector. It moves away from static reporting and provides clients with a real-time, machine-to-machine Operations Center interface.

**Key Features:**
* **RESTful Telemetry API:** Secure endpoint (`/api/device-ping/`) designed to ingest live JSON payloads from external hardware nodes (CCTV, Switches, Climate Sensors) and instantly sync to the database.
* **Google Single Sign-On (SSO):** Enterprise-grade authentication using OAuth 2.0 via `django-allauth`.
* **Interactive Data Grids:** Asynchronous, client-side asset tracking powered by `DataTables.js`, allowing instant pagination, sorting, and search filtering without page reloads.
* **Enterprise Admin Console:** A sleek, custom dark-themed administrative backend powered by Django `Jazzmin` for streamlined multi-tenant management.
* **Threat Analytics:** Interactive Doughnut chart built with `Chart.js` to break down active security alerts by severity (Critical, Warning, Info).

## Technology Stack

* **Backend:** Python 3, Django 5.x
* **Database:** SQLite (Development) / Ready for PostgreSQL (Production)
* **Authentication:** Django-Allauth (Google Provider / JWT)
* **Frontend:** HTML5, Bootstrap 5, Chart.js, DataTables.js
* **API Ingestion:** Native Django JSON parsing with CSRF exemption for automated hardware nodes


## Core Architecture

The database is built on highly relational Django models to link users directly to their localized security infrastructure:

* `DeviceHealth`: Monitors individual IoT and security hardware across multiple warehouse and office locations, updating via API.
* `SecurityAlert`: Logs physical and digital breaches with timestamps and resolution tracking.
* `ClientOutcome`: Tracks overall project health and system uptime metrics.

## 📡 API Integration: Hardware Ping Simulator

External network devices synchronize with the database by firing a POST request to the API gateway. 

**Endpoint:** `POST /api/device-ping/`

**Example JSON Payload:**
```json
{
  "device_id": 1,
  "status": "ONLINE",
  "firmware_version": "v4.2.1",
  "telemetry": {
    "cpu_usage_percent": 14.5,
    "uptime_hours": 128
  }
}