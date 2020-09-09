=========
 Roadmap
=========

Schedule
========

=========================   ==========  ===========
Version                     Date        Notes
=========================   ==========  ===========
0.5_                        11/17/2019  First Public Release
0.6_                        01/30/2020  Open source Release
0.7_                        03/26/2020  50% content
0.8_                        05/28/2020  80% content
0.8_                        06/26/2020  85% content
0.9_                        07/30/2020  Final Gold Preview
1.0_                        10/29/2020  Gold Release
`Provisional 1.1 Rev 1`_    12/17/2020  
`Provisional 1.1 Rev 2`_    03/25/2021
`Provisional 1.1 Rev 3`_    06/24/2021
`1.1 Rev 1`_                09/23/2021
=========================   ==========  ===========

Details:
========


0.6
---

We will publish:

- HTML and PDF on spec.oneapi.org
- Sources in github

No public announcement until we can ensure we are addressing earlier
feedback.

- Overall

  - New
  
    - Unified into single doc
    - PDF of unified doc available online
    - Sources in github.com/oneapi-src/oneapi-spec
    - HTML doc links back to github
    - CI builds and publishes on commits to master
- DPC++

  - New
  
    - Editing updates
    
  - Future

- oneDPL

  - New
  
    - Editing updates
  - Future
- oneDNN

  - New
  
    - API document inline
    - API document sources in oneapi-spec repo
  - Future
  
    - more structured API description
- oneCCL

  - New
  
    - API document inline
    - API document sources in oneapi-spec repo
- Level Zero

  - New
  
    - API document inline
    - Sources in separate repo on github
  - Future
- oneDAL

  - New
  - Future
  
    - API document included inline
    - API document sources in oneapi-spec repo
- oneTBB

  - New
  
    - API document inline
    - Sources in separate repo on github
  - Future
- oneVPL

  - New
  
    - API descriptions moved to single section
  - Future
  
    - Content?
- oneMKL

  - New
  - Future
  
    - Transition from far html to rst
    - API document inline    
    - rst sources included in oneapi-spec repo

0.7
---

Summary
+++++++

50% content.

Schedule
++++++++

=========  ==========
Date       Milestone
=========  ==========
3/12/2020  Cutoff date for accepting feedback for inclusion in this version
3/24/2020  Code freeze
3/26/2020  Release
=========  ==========

- Overall

  - All documents inline, no tarballs
  - Built from source from single repo
  - CI moved to public infrastructure, internal fork with CI for testing

- DPC++

  - Updated extensions table and description
  - TODO: more specific about extensions

- oneDPL

  - Rework the section for execution policies and buffer wrappers
  - Add API descriptions for oneDPL specific algorithms
  - Add API descriptions for iterator and functor classes

- oneDNN

  - API's 95% complete
  - Rework API presentation into multiple sections
  - Add introduction, execution, primitive lifecycle, and programming model
    sections

- Level Zero

  - Switched to RST as format, using oneapi-spec as upstream repo
  
- oneDAL

  - Add overall spec skeleton, introduction and algorithm classes sections
  - Add initial version for sections on data structures (descriptors algorithms/tables, numeric tables),
    compute modes(batch/online), distributed algorithms and generic building blocks(train/predict) 
  - Add API for 3 oneDAL algorithms

- oneTBB

  - Integrate sources to the oneapi-spec repository
  - Rework sections for general information, memory allocation, synchronization, and timing
  
- oneVPL
  
  - 80% content
    
- oneMKL

  - USM support
  - Skeleton of spec, breadown by domain
  - Sections that apply to all domains
  - subset of domains with high-level description and APIs, as determined by open source schedule
  
0.8
---

Summary
+++++++

80% content. All document structuring issues resolved. Content mostly complete with
placeholders for missing sections.

Schedule
++++++++

=========  ==========
Date       Milestone
=========  ==========
5/14/2020  Cutoff date for accepting feedback for inclusion in this version
5/26/2020  Code freeze
5/28/2020  Release
=========  ==========

- DPC++

  - Updated extensions table and description
  - TODO: more specific about extensions

- oneDPL

  - Specify USM support
  - Specify range-based API to the algorithms

- oneDNN

  - Add sections on primitive attributes, data types, and memory formats
  - Start extending individual primitives' pages with detailed information
    about underlying math and with usage examples

- oneCCL

  - Add page with API for multi-GPU
  - Add page with multi-GPU programming model
  - Extend page with collective operations

- Level Zero

  - Command queue groups, module linking, extensions, and improved profiling support
  
- oneDAL

  - Extend API description to kNN classification
  - Add first version for sections on error handling, namespaces, terminology, math notations
  - Extend numeric tables and data structure sections

- oneTBB

  - Rework sections for algorithms, flow graph, thread local storage

- oneVPL

  - Updates deferred to 0.8.5_
  
- oneMKL

  - All domains complete
  - Finalized BLAS, LAPACK domains
  - Draft suitable for review so we can distribute to reviewers before
    ISC (6/28/2020).

0.8.5
-----

Summary
+++++++

- oneVPL

  - Breaking changes introduced.
  
=========  ==========
Date       Milestone
=========  ==========
6/25/2020  All components have merged to master
6/26/2020  Release
=========  ==========

0.9
---

Summary
+++++++

Final Gold Preview. Expectation is that everything is done and only 
small edits will be made. Incorporates all external feedback.

Schedule
++++++++

=========  ==========
Date       Milestone
=========  ==========
7/16/2020  Cutoff date for accepting feedback for inclusion in this version
7/28/2020  Code freeze
7/30/2020  Release
=========  ==========

Elements
++++++++

- DPC++

  - Updated extensions table and description
  - TODO: more specific about extensions

- oneDPL

  - Specify C++ standard library APIs (or analogues) supported in DPC++ kernels
  - Specify all remaining and late-added extension APIs
  - Integrate all known feedback

- oneDNN

  - Finish extending individual primitives' pages with detailed information
    about underlying math and with usage examples
  - explanation of principles complete

- oneCCL

  - Finalize on sections content and details

- Level Zero

  - 1.0 release, support for OpenCL interoperability
  
- oneDAL

  - Extend algorithms section to cover Random Forest, K-Means, SVM, PCA algorithms
  - Finalize on sections content and details

- oneTBB

  - Rework sections for containers, task scheduler controls, exceptions
  - Integrate all known feedback

- oneVPL

- oneMKL

  - finalize FFT, sparse BLAS, RNG, and VM domains
  
1.0
---

Summary
+++++++

API's frozen: backwards compatible
changes at discretion of project owner, non-backwards compatible change by exception only

Schedule
++++++++

=========  ==========
Date       Milestone
=========  ==========
10/27/2020  Code freeze
10/29/2020  Release
=========  ==========

- Overall

  - Minor cleanup and integration of remaining feedback if any

Provisional 1.1 Rev 1
---------------------

Provisional 1.1 Rev 2
---------------------

Provisional 1.1 Rev 3
---------------------

1.1 Rev 1
---------

