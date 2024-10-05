export default function SmarTeqUserAuth() {
  return (
    <main className="flex items-center justify-center h-screen">
      <div className="block mx-auto w-2/4 bg-white rounded-lg border-2 border-sky-400">
        <div className="m-3 flex">
          {/* Email Field */}
          <div>
            <p>Please choose your profile to access Bhavesh's documents</p>
            <label for="email">Email</label>
            <div>
              <select
                id="email"
                name="email"
                placeholder="dsvsd"
                className="block w-full rounded-md border-0 p-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
              >
                <option>bhavesh.asana@outlook.com</option>
                <option>hr@smarteqsolutions.com</option>
              </select>
            </div>
            <p>Please choose one email from the drop down list</p>
          </div>
          {/* Submit Email */}
          <div>
            <button>Submit</button>
          </div>
        </div>
        <div>
          {/* OPT field */}
          {/* Submit OPT */}
        </div>

        
      </div>
    </main>
  );
}
