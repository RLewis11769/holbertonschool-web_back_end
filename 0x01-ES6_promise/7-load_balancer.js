export default function loadBalancer(chinaDownload, USDownload) {
  // Returns promise that resolves first of options (like a load balancer might use)

  return Promise.race([chinaDownload, USDownload]);
}
