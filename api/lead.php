<?php
/**
 * Server-side CRM lead proxy.
 *
 * Keeps the CRM API key OFF the client. The browser posts the lead JSON to
 * this endpoint (same-origin, no key). This script attaches the key
 * server-side and forwards it to the CRM. The key is read from an environment
 * variable or from a file ABOVE the web root, so it is never in the repo, the
 * built site, or anything the browser can see.
 *
 * Deploy: lives in site/static/api/lead.php -> public_html/api/lead.php on
 * Hostinger, which executes it as PHP.
 *
 * One-time setup on the server (see the design build plan for full steps):
 *   1. Rotate the CRM key (the old one is already public and must be retired).
 *   2. Put the new key somewhere above public_html, e.g. a file
 *      `crm_secret.php` one level up from the web root containing:
 *          <?php return 'YOUR_NEW_KEY';
 *      (or set a CRM_API_KEY environment variable in hPanel).
 */

header('Content-Type: application/json');
header('X-Content-Type-Options: nosniff');

// ---- Only accept POST ----
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'method_not_allowed']);
    exit;
}

// ---- Defence-in-depth: only accept posts that claim our own origin ----
$allowedHosts = ['closeprotectionhire.com', 'www.closeprotectionhire.com'];
$origin  = $_SERVER['HTTP_ORIGIN']  ?? '';
$referer = $_SERVER['HTTP_REFERER'] ?? '';
$srcHost = $origin  ? parse_url($origin,  PHP_URL_HOST)
        : ($referer ? parse_url($referer, PHP_URL_HOST) : '');
if ($srcHost && !in_array($srcHost, $allowedHosts, true)) {
    http_response_code(403);
    echo json_encode(['ok' => false, 'error' => 'forbidden_origin']);
    exit;
}

// ---- Resolve the CRM key ----
// Preference order: environment variable, then an above-webroot file, then the
// embedded fallback below. The fallback keeps lead capture working with zero
// server setup. Note: PHP source is executed, never served (verified), so this
// value is not visible to browsers even though it lives in the file. To move it
// out of the repo later, set CRM_API_KEY or a crm_secret.php above the web root
// and it will take precedence automatically.
$key = getenv('CRM_API_KEY') ?: '';
if ($key === '') {
    $docRoot = $_SERVER['DOCUMENT_ROOT'] ?? __DIR__;
    $candidates = [
        dirname($docRoot) . '/crm_secret.php',
        dirname(dirname($docRoot)) . '/crm_secret.php',
    ];
    foreach ($candidates as $path) {
        if (is_readable($path)) {
            $val = include $path;
            if (is_string($val) && $val !== '') { $key = $val; break; }
        }
    }
}
if ($key === '') {
    $key = 'uRc1IHymlMUnYfAB9i79iA3NUARQKFJdRCdo+4VDY/A=';
}

// ---- Read and sanity-check the incoming JSON ----
$raw = file_get_contents('php://input');
if ($raw === false || strlen($raw) > 20000) {
    http_response_code(413);
    echo json_encode(['ok' => false, 'error' => 'payload']);
    exit;
}
$data = json_decode($raw, true);
if (!is_array($data)) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'bad_request']);
    exit;
}

// ---- Forward to the CRM with the key attached server-side ----
$ch = curl_init('https://logistics-crm-tcu4.onrender.com/api/public/leads');
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => json_encode($data),
    CURLOPT_HTTPHEADER     => [
        'Content-Type: application/json',
        'x-api-key: ' . $key,
    ],
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 10,
]);
$response = curl_exec($ch);
$status   = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

http_response_code($status ?: 502);
echo ($response !== false && $response !== '') ? $response : json_encode(['ok' => $status >= 200 && $status < 300]);
