
        <div class="page-header">
          <h2>About beautiful-data</h2>
        </div>

        <p class="lead" style="text-align:justify;">beautiful-data (BD) is an Open Source project that focuses on a large-scale data processing and visualization.  Its ultimate goal is to provide researchers, business analysts and students a software framework for working with "big data" in relatively short order.</p>
        
        <h3>The Stages of beautiful-data</h3>

        <p>We frame the BD's big data management process as a four-stage workflow, where each of the stages is responsible for a specific high-level task.</p>
        
        <ol>
           <li> <b>Data Aquisition</b>. The first stage is the acquisition of data.  BD does not impose any restrictions on how/where the data comes from.  Instead, it provides a consistent mechanism for users to acquire data.</li>
           <li> <b>Data Storage</b>.  The second stage involves storing the newly acquired data.  In its default settings, BD supports HDFS.  This means that, with minimum tweaking, a user can scale their data collection to a size that is only limited by the available hardware.</li>
           <li> <b>Data Analysis</b>.  The third stage is the heart of any big data operation: the analysis phase.  Out of the box, BD includes tools for doing simple data processing and statistical analysis.  These tools can drive BD analyses on a single node computer (e.g., a laptop computer) or be configured perform production runs on a highly scalable MapReduce cluster.</li>
           <li> <b>Data Visualization</b>. The final stage is the visualization of analyzed data a meaningful way.  BD delivers, at the end of its product toolchain, a static HTML report and/or "weblet" nuggets that can be easily integrated into any report format.</li>
        </ol>

		<h3>Software Framework</h3>		

        <p>BD is a continuously improving software framework that includes both the complete suite of data management applications and the underlying API layer.  For this reason, the BD design is <em>extremely</em> flexible and as it provides a robust pathway to support many extension points.</p>
