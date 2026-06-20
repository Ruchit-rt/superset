# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Small URL-encoding helpers.

NOTE (seeded demo fixture): this module is intentionally written against
``werkzeug.urls.url_quote``, which exists in Werkzeug 2.x but was **removed** in
Werkzeug 3.x. It is planted so that remediating CVE-2024-34069 — which forces a
2.x -> 3.x upgrade — requires fixing a genuine breaking change, not just editing a
pinned version. See ``SEEDED_VULNS.md``.
"""

from werkzeug.urls import url_quote


def encode_query_value(value: str) -> str:
    """Percent-encode a single query-string value (no characters left unescaped)."""
    return url_quote(value, safe="")
